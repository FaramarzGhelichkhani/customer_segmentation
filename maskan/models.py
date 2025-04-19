from django.db import models
from utils.validators import validate_length
from utils.jalalidate import JalaliDateField
from customer.models import Customer

class PostMap(models.Model):
    postalcode = models.CharField(max_length=6, null=False, db_index=True ,validators=[validate_length]) # 6 digit
    city = models.CharField(max_length=128, null=True,  blank=True)
    neighborhood =  models.CharField(max_length=128, null=True,  blank=True)
    average_price = models.BigIntegerField(null=True, blank=True)
    insert_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.postalcode}_{self.city}_{self.neighborhood}"

    class Meta:
        verbose_name = "Postal Map"
        verbose_name_plural = "Postal Maps"
        db_table = "postal_map"
        ordering = ["postalcode"]
        constraints = [models.UniqueConstraint("postalcode", "city", "neighborhood", name='unique_row')]

class GnafBuildings(models.Model):
    buildingid   = models.IntegerField(primary_key=True, db_index=True)
    parcel       = models.JSONField(null=True)
    geom         = models.JSONField(null=True)
    state_name   =  models.CharField(max_length=64, null=False)
    locationtype= models.CharField(max_length=32, null=False)
    locationname = models.CharField(max_length=128, null=False)
    parish       = models.CharField(max_length=256, null=True)
    tour       = models.CharField(max_length=5, null=True)

    def __str__(self):
        return f"{self.buildingid}"

    class Meta:
        db_table = "gnaf_buildings"

class GnafUnits(models.Model):
    building = models.ForeignKey(GnafBuildings, on_delete=models.DO_NOTHING, related_name='units', null=False, db_index=True)
    avenue   = models.TextField(null=True)
    preaventypename= models.CharField(max_length=32, null=True)
    preaven = models.TextField(null=True)
    floorno = models.IntegerField(null=True) # floor number of this unit 
    tour    = models.CharField(max_length=5, null=True)
    plate_no= models.IntegerField(null=False) # plaque
    unit = models.CharField(max_length=64, null=True)
    activity = models.TextField(null=True)
    postalcode = models.CharField(max_length=10, null=False)
    address = models.TextField(null=True)

    def __str__(self):
        return f"unit for building: {self.building}"

    class Meta:
        db_table = "gnaf_units"
        constraints = [models.UniqueConstraint("postalcode", name='unique_postalcode')]

class AmlakRent(models.Model):
    postal_code = models.CharField(max_length=10, null=False, db_index=True)
    insert_time = models.DateTimeField(auto_now_add=True)
    trace_id_date = JalaliDateField(null=True)
    contract_code = models.CharField(max_length=32, blank=True, null=True)
    estate_types_name = models.CharField(max_length=64, blank=True, null=True)
    usage_types_name = models.TextField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    quota = models.IntegerField(blank=True, null=True)
    price_rahn = models.BigIntegerField(blank=True, null=True)
    price_monthly = models.BigIntegerField(blank=True, null=True)
    price_per_m2 = models.BigIntegerField(blank=True, null=True)
    sale_sakht = models.IntegerField(blank=True, null=True)
    frame_types_name = models.TextField(blank=True, null=True)
    frontage_type_name = models.TextField(blank=True, null=True)
    bedroom_count = models.IntegerField(blank=True, null=True)
    unit_floor_side_name = models.CharField(max_length=16, blank=True, null=True)
    tel_status_name = models.BooleanField(blank=True, null=True)
    parking_status = models.BooleanField(blank=True, null=True)
    elevator_status = models.BooleanField(blank=True, null=True)
    warehouse_status = models.BooleanField(blank=True, null=True)
    floors_count = models.IntegerField(blank=True, null=True)
    floor_no = models.IntegerField(blank=True, null=True)
    unit_per_floor = models.IntegerField(blank=True, null=True)
    subscription_status = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.estate_types_name}__{self.usage_types_name}"

    class Meta:
        verbose_name = "Amlak Rent"
        verbose_name_plural = "Amlaks Rent"
        db_table = "amlak_rents"
        ordering = ["-trace_id_date"]

class AmlakSale(models.Model):
    postal_code = models.CharField(max_length=10, null=False, db_index=True)
    insert_time = models.DateTimeField(auto_now_add=True)
    trace_id_date = JalaliDateField(null=True)
    contract_code = models.CharField(max_length=32, blank=True, null=True)
    estate_types_name = models.CharField(max_length=64, blank=True, null=True)
    usage_types_name = models.TextField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    quota = models.IntegerField(blank=True, null=True)
    price  = models.BigIntegerField(blank=True, null=True)
    price_per_m2 = models.BigIntegerField(blank=True, null=True)
    sale_sakht = models.IntegerField(blank=True, null=True)
    frame_types_name = models.TextField(blank=True, null=True)
    frontage_type_name = models.TextField(blank=True, null=True)
    unit_floor_side_name = models.CharField(max_length=16, blank=True, null=True)
    tel_status_name = models.BooleanField(blank=True, null=True)
    parking_status = models.BooleanField(blank=True, null=True)
    elevator_status = models.BooleanField(blank=True, null=True)
    warehouse_status = models.BooleanField(blank=True, null=True)
    floors_count = models.IntegerField(blank=True, null=True)
    floor_no = models.IntegerField(blank=True, null=True)
    unit_per_floor = models.IntegerField(blank=True, null=True)
    subscription_status = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.estate_types_name}__{self.usage_types_name}"

    class Meta:
        verbose_name = "Amlak Sale"
        verbose_name_plural = "Amlaks Sale"
        db_table = "amlak_sales"
        ordering = ["-trace_id_date"]

class MaskanValueEstimation(models.Model):
    customer_key= models.OneToOneField(Customer, null=False, on_delete=models.DO_NOTHING, related_name='maskan_estimation', db_index=True, unique=True) 
    insert_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    unit = models.IntegerField(null=True, blank=True)  # number of unit  for buildingid 
    floor = models.IntegerField(null=True, blank=True) # number of floor for  building 
    mode_unit_per_floor = models.IntegerField(null=False, blank=True)
    prediction_area = models.FloatField(null=True , blank=True)
    prediction_area_price_per_m2 = models.BigIntegerField(null=True,  blank=True)

    class Meta:
        db_table= "unit_estimation"
       