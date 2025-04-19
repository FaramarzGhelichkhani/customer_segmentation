from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from customer.models import Customer  
from customer.utils.registration import Registration
from maskan.models import GnafUnits, MaskanValueEstimation  

class Command(BaseCommand):
    help = 'Register customers who are not registered yet within the past number of days.'

    def add_arguments(self, parser):
        parser.add_argument('days', type=int, help='The number of days to look back for unregistered customers.')

    def handle(self, *args, **kwargs):
        days = kwargs['days']
        date_threshold = timezone.now() - timedelta(days=days)
        self.stdout.write(self.style.SUCCESS(f'customers registeration start for {days} day(s) past.'))

        unregistered_customers = Customer.objects.filter(registration=False, insert_time__gte=date_threshold)
        
        if unregistered_customers.exists():
            registration_instance = Registration(customers=unregistered_customers)
            registration_instance.base_algorithm()
        else:
            self.stdout.write(self.style.WARNING('no customers found for registeration.'))
        self.stdout.write(self.style.SUCCESS('customers registeration command done.'))
