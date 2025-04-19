from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not self.get_preserved_filters(request): 
            return qs.filter(customer_key__lte=200)
        return qs 
    list_display = ['registerdate','customer_key', 'address_validation', 'registration']
    search_fields = ['postalcode','phone_number', 'customer_key']
    readonly_fields = ['insert_time']
    list_filter  = ('gendercode', 'job_title')
    ordering = ['-registerdate']
    
admin.site.register(Customer, CustomerAdmin)
