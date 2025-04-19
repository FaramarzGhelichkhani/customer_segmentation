from django.db import models
from utils.jalalidate import JalaliDateField
from utils.validators import gender_validator, age_validator, postal_code_validator


class Customer(models.Model):
    customer_key = models.BigAutoField(primary_key=True, db_index=True)
    customerCode = models.PositiveBigIntegerField(unique=True, db_index=True, null=True)
    registerdate = JalaliDateField(null=True, blank=True)
    birthdate = JalaliDateField(null=True, blank=True)
    birthdatekey = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    postalcode = models.CharField(
        max_length=10, null=True, blank=True, validators=[postal_code_validator]
    )
    nationalcode = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    registration = models.BooleanField(null=True, blank=True)
    address_validation = models.BooleanField(null=True, blank=True)
    job_title = models.CharField(max_length=64, null=True, blank=True)
    address = models.TextField(max_length=64, null=True, blank=True)
    gendercode = models.IntegerField(
        default=1, validators=[gender_validator], null=True, blank=True
    )
    insert_time = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    customer_type_code = models.IntegerField(null=True, blank=True)
    party_type_code = models.IntegerField(null=True, blank=True)
    organizationalcode = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return f"{self.customer_key}"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        db_table = "customer"
