from maskan.models import GnafUnits
from maskan.utils.address_process import FeatureExtractor

class Validation:
    def __init__(self, customers=[]) -> None:
        self.customers = customers
        self.addressprocessor=FeatureExtractor()

    def customers_address_validation(self):
        for customer in self.customers:
            if (customer.address_validation is None or customer.address_validation == False) and customer.address is not None and customer.address != '':
                customer.address_validation =  self.customer_address_validation(customer)
                customer.save()

    def customer_address_validation(self, customer):
        """
        args: a customer object
        return: True or False. if postal code is not available in Gnaf it return None.
        """
        unit_objs = GnafUnits.objects.filter(postalcode=customer.postalcode)
        if unit_objs.exists():
            unit_obj = unit_objs[0]
            # extract  paluqu of addresses 
            customer_plaque = self.addressprocessor.extract_plaque(address=customer.address) 
            unit_plaque = abs(unit_obj.plate_no) # plate_no is integer and null=False

            if customer_plaque == str(unit_plaque) and unit_plaque !=0 and customer_plaque is not None:
                return True
            
            # extract unit           
            unit_unit = unit_obj.unit
            customer_unit = self.addressprocessor.extract_unit(address=customer.address) 
            if unit_plaque !=0 :
                if customer_unit == str(unit_plaque):
                    return True
            
            if customer_unit == unit_unit and customer_unit is not None and unit_unit is not None:
                return True

            # extract floor           
            unit_floor = unit_obj.floorno
            customer_floor = self.addressprocessor.extract_floor(address=customer.address)
            if customer_floor == str(unit_floor) and customer_floor is not None and unit_floor is not None:
                return True 
            
            return False
        
        return None 
        