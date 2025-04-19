from django.db import models
from customer.models import Customer

class SimCard(models.Model):
    insert_time = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=11, null=False, db_index=True, unique=True)
    simtype = models.CharField(max_length=128, null=True, blank=True)
    simoperator = models.CharField(max_length=128, null=True,  blank=True)
    simqualitytypeid =  models.CharField(max_length=128, null=True,  blank=True)
    price = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Sim Card"
        verbose_name_plural = "Sim Cards"
        db_table = "sim_card"
    

class SimCardValueEstimation(models.Model):
    insert_time = models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now=True)
    customer= models.ForeignKey(Customer, null=False, on_delete=models.DO_NOTHING, related_name='simcard_estimation', db_index=True) 
    sim_number =  models.CharField(max_length=11, null=False, db_index=True)
    estimated_price = models.BigIntegerField(null=False)

    def __str__(self):
        return self.sim_number

    class Meta:
        verbose_name = "Sim Card Value"
        verbose_name_plural = "Sim Cards Value"
        db_table = "sim_card_estimation"
        constraints = [models.UniqueConstraint("customer", "sim_number", name='unique_customer_sim')]

