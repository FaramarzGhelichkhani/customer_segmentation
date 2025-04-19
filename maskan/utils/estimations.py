import joblib
import pandas as pd 
import numpy as np
from django.db.models import Count, Max, Min
from customer_segmentation.settings import BASE_DIR
from maskan.models import GnafUnits, PostMap
from area import area
from collections import Counter
from django.db.models import Q

PATH =  BASE_DIR.as_posix() + "/data/models/"

class AreaEstimation:
    
    def __init__(self) -> None:
        self.models= {'تهران':joblib.load(PATH+'/xgboost_model_unit_area_tehran.pth'),
                     'تبریز':joblib.load(PATH+'/xgboost_model_unit_area_tabriz.pth'),
                      'شیراز':joblib.load(PATH+'/xgboost_model_unit_area_shiraz.pth'),
                      'کرج':joblib.load(PATH+'/xgboost_model_unit_area_karaj.pth')
                      } 
    
    def _get_mode_of_floor(self, gnaf_unit_instance):
        building = gnaf_unit_instance.building

        unit_per_floor = (
            GnafUnits.objects
            .filter(building=building) 
            .values('floorno')
            .annotate(unit_per_floor=Count('id')) 
        )

        mode_unit_of_floors = Counter(list(unit_per_floor.values_list('unit_per_floor', flat=True))).most_common(1)[0][0]
        return  mode_unit_of_floors
    
    def _cal_area(self, parcel):
        if not  parcel is None:
            return round(area(parcel), 2)
        else:
            raise ValueError("parcel is None")
            # return None
        
    def _get_agg_data(self, gnaf_unit_instance):
        out =  {}
        building = gnaf_unit_instance.building
        grouped = GnafUnits.objects.filter(building=building).values('building')
        out["floor"] = grouped.annotate(floor=(Max('floorno') - Min('floorno')))[0]['floor'] + 1
        out["unit"] = grouped.annotate(unit=Count('id'))[0]['unit']
        return out 

    def get_unit_featurs(self, gnaf_unit_instance):
        """
        arg: gnagunit obj
        return: dict contain mode_unit_per_floor, landarea, floor, unit
        """
        result = {}
        get_mode_of_floor = self._get_mode_of_floor(gnaf_unit_instance)
        land_area = self._cal_area(gnaf_unit_instance.building.parcel)
        agg = self._get_agg_data(gnaf_unit_instance)
        result["mode_unit_per_floor"] =  get_mode_of_floor
        result["landarea"] =  land_area
        result["city"] = gnaf_unit_instance.building.locationname
        return {**result, **agg}
    
    def get_predict(self, dict_feature):
        city = dict_feature['city']
        df = pd.DataFrame([dict_feature])
        if city in ('تهران','تبریز','شیراز','کرج') and dict_feature['landarea'] is not None:
            model = self.models[city]
            x =  df[model.feature_names_in_]
            pred = model.predict(x)
            return round(float(pred),2)
        else:
            raise ValueError("Area Estimation is not supported for this city")

class HomeValueEstimation:

    def __init__(self) -> None:
        self.models= {'تهران':joblib.load(PATH+'/xgboost_home_value_tehran.pkl'),
                     'تبریز':joblib.load(PATH+'/xgboost_home_value_tabriz.pkl'),
                      'شیراز':joblib.load(PATH+'/xgboost_home_value_shiraz.pkl'),
                      'کرج':joblib.load(PATH+'/xgboost_home_value_karaj.pkl')
                      } 

    def get_features(self, unit_obj, area_obj=None):
        """
        return dict feature for a postalcode  
        """

        area_obj = AreaEstimation() if area_obj is None else area_obj
        area_feature_dictionary = area_obj.get_unit_featurs(unit_obj)
        area_predict = area_obj.get_predict(area_feature_dictionary)
        postmap = PostMap.objects.filter(Q(postalcode=unit_obj.postalcode[:6]) | Q(postalcode=unit_obj.postalcode[:5]))[0]
        return {**area_feature_dictionary, **{'neighborhood': postmap.neighborhood, 'average_price':postmap.average_price}, **{'area': area_predict}}
        
    def get_predict(self, feature):
        city = feature['city'] 
        feature_dict = {'floors_count': feature['floor'], 'unit_per_floor': feature['mode_unit_per_floor']\
                   ,'weighted_average_price':feature['average_price'], **feature }
        if city in ('تهران', 'تبریز','شیراز','کرج'):
            df = pd.DataFrame([feature_dict])
            df["neighborhood"] = df["neighborhood"].astype('category')
            model = self.models[city]
            x =  df[model.feature_names_in_]
            pred = model.predict(x) # log
            pred = np.exp(pred)
            return  round(float(pred),2)
        else:
            raise ValueError("Area Estimation is not supported for this city")
        