from maskan.utils.postalcode_validation import Validation
from simcard.utils.estimation import SimValueEstimation
from simcard.models import SimCardValueEstimation
from maskan.utils.estimations import HomeValueEstimation, AreaEstimation
from maskan.models import MaskanValueEstimation, GnafUnits
from django.utils import timezone

class Registration:
    
    def __init__(self, customers) -> None:
        self.customers = customers
        self.simcard_estimation_object= SimValueEstimation()
        self.area_estimation_object = AreaEstimation()
        self.maskan_estimation_object = HomeValueEstimation()
        self.simcardestimationobjects = []
        self.homeestimationobjects = []
    
    def base_algorithm(self):
        self.address_validation()
        self.home_value_estimation()
        self.simcard_value_estimation()
        self.save_objs()
    
    def address_validation(self):
        address_vaildaion_object = Validation(customers=self.customers)
        address_vaildaion_object.customers_address_validation()
    
    def home_value_estimation(self):
        for customer in self.customers:
            try:
                home_estimation_obj = self.home_value_estimation_customer(customer=customer)
                if home_estimation_obj is not None:
                    self.homeestimationobjects.append(home_estimation_obj)    
            except Exception as e:
                print(e)
                continue

    def _get_unit(self,customer):
        try:
            postalcode = customer.postalcode
            if postalcode is None or len(postalcode) < 10:
                raise ValueError(f"postal code is not valid. {postalcode}")
            gnafunit = GnafUnits.objects.get(postalcode=postalcode)
            return gnafunit
        except Exception as e:
            print(e)

    def _get_maskan_estimation_attributes(self, gnaf_unit_obj):
        if gnaf_unit_obj.building.locationname in  ('تهران', 'تبریز','شیراز','کرج'):
            feature_dict =  self.maskan_estimation_object.get_features(gnaf_unit_obj, self.area_estimation_object)
            pred = self.maskan_estimation_object.get_predict(feature_dict)
            return {"prediction_area_price_per_m2":pred, "prediction_area":feature_dict["area"], **feature_dict}
        return None 

    def home_value_estimation_customer(self, customer):
        if customer.address_validation:
                gnafunit = self._get_unit(customer)
                args = self._get_maskan_estimation_attributes(gnafunit)
                if args is not None:
                    obj = MaskanValueEstimation(customer_key=customer, **{key: value for key, value in args.items() if key in MaskanValueEstimation.__dict__})
                    return obj
        else:
            print(f"addres is not valid. for {customer}")
        return None
    
    def simcard_value_estimation_customer(self, customer):
        phone_number = customer.phone_number
        if phone_number is not None and len(phone_number) == 11:
            pred = self.simcard_estimation_object.get_predict(phone_number)
            obj = SimCardValueEstimation(sim_number=phone_number, estimated_price=pred, customer=customer)
            return obj
        else:
            print(f"phone number is not valid. {phone_number}")
        return None
        
    def simcard_value_estimation(self):
        for customer in self.customers:
            try:
                simcard_estimation_obj =  self.simcard_value_estimation_customer(customer)
                if simcard_estimation_obj is not None:
                    self.simcardestimationobjects.append(simcard_estimation_obj)
            except Exception as e:
                print(e)
                continue

    def save_objs(self):
        # maskan estimation 
        for obj in self.homeestimationobjects:
            _ , created = MaskanValueEstimation.objects.update_or_create(
            customer_key=obj.customer_key,
            defaults={
                'unit': obj.unit,
                'floor': obj.floor,
                'mode_unit_per_floor': obj.mode_unit_per_floor,
                'prediction_area': obj.prediction_area,
                'prediction_area_price_per_m2': obj.prediction_area_price_per_m2,
                'update_time': timezone.now(), 
            }
        )
        print(f"number of maskan estimation instance {len(self.homeestimationobjects)}")
        # simcard estimation
        for estimation in self.simcardestimationobjects:
            _, created = SimCardValueEstimation.objects.update_or_create(
                customer=estimation.customer,
                sim_number=estimation.sim_number,
                defaults={
                    'estimated_price': estimation.estimated_price,
                    'update_time': timezone.now(), 
                }
            )
        print(f"number of simcard estimation instance {len(self.simcardestimationobjects)}")
        # customers
        for customer in self.customers:
            customer.registration = True
            customer.save()
        print(f"{len(self.customers)} of customer registered.")
        