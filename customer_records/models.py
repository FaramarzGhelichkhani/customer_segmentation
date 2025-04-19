from django.db import models
from customer.models import Customer
from django.contrib.postgres.fields import ArrayField
from django.db.models import  JSONField

class Lawyer(models.Model):
    customerkey = models.OneToOneField(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="lawyer",
        db_index=True,
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    officephone = models.CharField(max_length=11, null=True, blank=True)
    status = models.CharField(max_length=50, default="active", null=True)
    grade = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "lawyer"
        verbose_name_plural = "lawyers"
        db_table = "lawyers"
        constraints = [
            models.UniqueConstraint(
                "name", "phone_number", name="lawyer_name_phone_number"
            )
        ]


class Doctor(models.Model):
    customerkey = models.OneToOneField(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="doctor",
        db_index=True,
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    takhasos = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    jens = models.CharField(max_length=4, null=True, blank=True)
    birthdatekey = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    nezam_pezeshki = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "doctor"
        verbose_name_plural = "doctors"
        db_table = "doctors"
        constraints = [
            models.UniqueConstraint(
                "name", "phone_number", name="doctor_name_phone_number"
            )
        ]


class GoldSeller(models.Model):
    customerkey = models.OneToOneField(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="gold_seller",
        db_index=True,
    )
    senf = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "gold seller"
        verbose_name_plural = "gold sellers"
        db_table = "gold_seller"
        constraints = [
            models.UniqueConstraint(
                "name", "phone_number", name="goldseller_name_phone_number"
            )
        ]


class Agent(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="agent",
        db_index=True,
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    nationalcode = models.CharField(max_length=10, null=True, blank=True)
    active = models.BooleanField(default=True, null=True)
    startdatekey = models.IntegerField(null=True, blank=True)
    enddatekey = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "agent"
        verbose_name_plural = "agents"
        db_table = "agents"
        constraints = [
            models.UniqueConstraint(
                "name",
                "phone_number",
                "customerkey",
                name="agent_name_phone_number_customerkey",
            )
        ]


class Rasmio(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="rasmio",
        db_index=True,
    )
    nationalcode = models.CharField(max_length=10)
    full_name = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    is_valid_nationalcode = models.BooleanField(default=False)
    is_male = models.BooleanField(default=True, null=True, blank=True)
    companies_count = models.IntegerField(default=0)
    company_id = models.CharField(max_length=20, null=True, blank=True)
    company_title = models.CharField(max_length=255, null=True, blank=True)
    position_title = models.CharField(max_length=128, null=True, blank=True)
    first_role = models.CharField(max_length=32, null=True, blank=True)
    second_role = models.CharField(max_length=32, blank=True, null=True)
    representing_title = models.CharField(max_length=128, blank=True, null=True)
    representing_id = models.CharField(max_length=24, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    first_presence = models.DateField(blank=True, null=True)
    void_date = models.DateField(blank=True, null=True)
    by_latest_news = models.BooleanField(default=False, blank=True, null=True)
    is_finished = models.BooleanField(default=False)
    void_by_news_id = models.CharField(max_length=12, blank=True, null=True)
    by_news_id = models.CharField(max_length=10, blank=True, null=True)
    all_roles = ArrayField(
        models.TextField(blank=True), blank=True, null=True
    )  # PostgreSQL text[]
    fetch_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "rasmio"
        verbose_name_plural = "rasmio"
        db_table = "rasmio"


class BamaCar(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="bama",
        db_index=True,
    )

    ad_id = models.CharField(max_length=8, null=True, blank=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    price = models.BigIntegerField(blank=True, null=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    brand = models.CharField(max_length=32, null=True, blank=True)
    model = models.CharField(max_length=32, null=True, blank=True)
    trim = models.CharField(max_length=256, null=True, blank=True)
    gear_box = models.CharField(max_length=16, null=True, blank=True)
    prod_year = models.IntegerField(blank=True, null=True)
    usage_km = models.IntegerField(blank=True, null=True)
    body_type = models.CharField(max_length=32, null=True, blank=True)
    body_status = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    neighborhood = models.CharField(max_length=32, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    authenticated = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "bama"
        verbose_name_plural = "bama"
        db_table = "bama"


class SheypoorCar(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="sheypoor_car",
        db_index=True,
    )

    ad_id = models.CharField(max_length=32, null=True, blank=True)
    title = models.CharField(max_length=512, null=True, blank=True)
    url = models.CharField(max_length=512, null=True, blank=True)
    province = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    neighborhood = models.CharField(max_length=128, null=True, blank=True)
    brand = models.CharField(max_length=128, null=True, blank=True)
    price = models.BigIntegerField(blank=True, null=True)
    chasis = models.CharField(max_length=32, null=True, blank=True)
    production_year = models.CharField(max_length=16, null=True, blank=True)
    usage = models.CharField(max_length=32, null=True, blank=True)
    gear = models.CharField(max_length=32, null=True, blank=True)
    body_status = models.CharField(max_length=64, null=True, blank=True)
    model = models.CharField(max_length=32, null=True, blank=True)
    date = models.CharField(max_length=32, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    seller_name = models.CharField(max_length=128, null=True, blank=True)
    reg_date = models.CharField(max_length=32, null=True, blank=True)
    seller_profile = models.CharField(max_length=128, null=True, blank=True)
    version = models.CharField(max_length=32, null=True, blank=True)
    currency = models.CharField(max_length=32, null=True, blank=True)
    full_attr = models.CharField(max_length=512, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "sheypoor_car"
        verbose_name_plural = "sheypoor_car"
        db_table = "sheypoor_car"


class SheypoorHomeRent(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="sheypoor_homerent",
        db_index=True,
    )

    ad_id = models.CharField(max_length=32, null=True, blank=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    url = models.CharField(max_length=128, null=True, blank=True)
    province = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    neighborhood = models.CharField(max_length=32, null=True, blank=True)
    area = models.CharField(max_length=32, null=True, blank=True)
    mortgage = models.CharField(max_length=32, null=True, blank=True)
    rent = models.CharField(max_length=32, null=True, blank=True)
    rent_type = models.CharField(max_length=8, null=True, blank=True)
    room = models.CharField(max_length=16, null=True, blank=True)
    parking = models.CharField(max_length=8, null=True, blank=True)
    storage = models.CharField(max_length=8, null=True, blank=True)
    elevator = models.CharField(max_length=8, null=True, blank=True)
    age = models.CharField(max_length=16, null=True, blank=True)
    date = models.CharField(max_length=16, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    seller_name = models.CharField(max_length=128, null=True, blank=True)
    reg_date = models.CharField(max_length=16, null=True, blank=True)
    seller_profile = models.CharField(max_length=64, null=True, blank=True)
    full_attr = models.CharField(max_length=2048, null=True, blank=True)
    location = models.CharField(max_length=128, null=True, blank=True)
    price = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "sheypoor_homerent"
        verbose_name_plural = "sheypoor_homerent"
        db_table = "sheypoor_homerent"


class SheypoorHomeSale(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="sheypoor_homesale",
        db_index=True,
    )

    ad_id = models.CharField(max_length=16, null=True, blank=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    url = models.CharField(max_length=128, null=True, blank=True)
    province = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    neighborhood = models.CharField(max_length=32, null=True, blank=True)
    area = models.CharField(max_length=16, null=True, blank=True)
    price = models.CharField(max_length=16, null=True, blank=True)
    price_sqrm = models.CharField(max_length=16, null=True, blank=True)
    ad_type = models.CharField(max_length=16, null=True, blank=True)
    room = models.CharField(max_length=16, null=True, blank=True)
    parking = models.CharField(max_length=8, null=True, blank=True)
    storage = models.CharField(max_length=8, null=True, blank=True)
    elevator = models.CharField(max_length=8, null=True, blank=True)
    age = models.CharField(max_length=16, null=True, blank=True)
    date = models.CharField(max_length=16, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    seller_name = models.CharField(max_length=128, null=True, blank=True)
    reg_date = models.CharField(max_length=16, null=True, blank=True)
    seller_profile = models.CharField(max_length=64, null=True, blank=True)
    location = models.CharField(max_length=128, null=True, blank=True)
    full_attr = models.CharField(max_length=2048, null=True, blank=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "sheypoor_homesale"
        verbose_name_plural = "sheypoor_homesale"
        db_table = "sheypoor_homesale"


class SheypoorVillaSale(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="sheypoor_villasale",
        db_index=True,
    )

    ad_id = models.CharField(max_length=16, null=True, blank=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    url = models.CharField(max_length=128, null=True, blank=True)
    province = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    neighborhood = models.CharField(max_length=32, null=True, blank=True)
    area = models.CharField(max_length=32, null=True, blank=True)
    price = models.CharField(max_length=16, null=True, blank=True)
    price_sqrm = models.CharField(max_length=16, null=True, blank=True)
    room = models.CharField(max_length=16, null=True, blank=True)
    parking = models.CharField(max_length=8, null=True, blank=True)
    storage = models.CharField(max_length=8, null=True, blank=True)
    balcony = models.CharField(max_length=8, null=True, blank=True)
    age = models.CharField(max_length=16, null=True, blank=True)
    date = models.CharField(max_length=16, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    seller_name = models.CharField(max_length=64, null=True, blank=True)
    reg_date = models.CharField(max_length=16, null=True, blank=True)
    seller_profile = models.CharField(max_length=64, null=True, blank=True)
    location = models.CharField(max_length=64, null=True, blank=True)
    full_attr = models.CharField(max_length=2048, null=True, blank=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "sheypoor_villasale"
        verbose_name_plural = "sheypoor_villasale"
        db_table = "sheypoor_villasale"

class PazirehNevisi(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="pazireh",
        db_index=True,
    )
    issuerkey = models.IntegerField(null=False)
    issuerSymbol = models.CharField(max_length=32,null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "pazireh_neveisi"
        verbose_name_plural = "pazireh_neveisi"
        db_table = "pazireh_neveisi"

class ArzeAvvalieh(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="arze_avvalieh",
        db_index=True,
    )
    issuerkey = models.IntegerField(null=False)
    stockKey = models.IntegerField(null=False)
    issuerSymbol = models.CharField(max_length=32,null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unitPrice = models.BigIntegerField(null=True, blank=True)
    firstTradeDateKey = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "arze_avvalieh"
        verbose_name_plural = "arze_avvalieh"
        db_table = "arze_avvalieh"


class YadDasht(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="yaddasht",
        db_index=True,
    )
    isin = models.CharField(max_length=32,null=True, blank=True)
    comment=models.CharField(max_length=512,null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.customerkey

    class Meta:
        verbose_name = "yaddasht"
        verbose_name_plural = "yaddasht"
        db_table = "yaddasht"

class Linka(models.Model):
    customerkey = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="linka",
        db_index=True,
    )
    standard_name = models.CharField(max_length=500, null=True)
    company_type_id = models.IntegerField(null=True)
    company_type_description = models.CharField(max_length=500)
    state_id = models.IntegerField(null=True)
    state_description = models.CharField(max_length=500)
    company_national_code = models.CharField(max_length=50)
    register_number = models.CharField(max_length=50, null=True)  
    economic_code = models.CharField(max_length=50, null=True)  
    bourse_symbol = models.CharField(max_length=250, null=True)  
    phone_number = models.CharField(max_length=50, null=True)  
    post_code = models.CharField(max_length=50, null=True)  
    address_desc = models.TextField(null=True)  
    lat = models.DecimalField(max_digits=10, decimal_places=7, null=True)  
    long = models.DecimalField(max_digits=10, decimal_places=7, null=True)  
    email_address = models.EmailField(max_length=255, null=True)  
    parent_count = models.IntegerField(null=True)
    child_count = models.IntegerField(null=True)
    count_portfo = models.IntegerField(null=True)
    gazette_stock = models.FloatField(null=True)  
    last_change = JSONField(null=True)  

    def __str__(self):
        return self.standard_name
    
    class Meta:
        verbose_name = "Linka"
        verbose_name_plural = "Linka"
        db_table = "linka"
