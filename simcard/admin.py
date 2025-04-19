from django.contrib import admin
from .models import SimCard, SimCardValueEstimation

class SimCardAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not self.get_preserved_filters(request): 
            return qs.filter(id__lte=200)
        return qs 
    list_display = ['insert_time', 'number', 'simtype', 'simoperator', 'simqualitytypeid', 'price']
    search_fields = ['number']
    readonly_fields = ['insert_time']
    list_filter = ('simtype', 'simoperator', 'simqualitytypeid')

class SimCardValueEstimationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not self.get_preserved_filters(request): 
            return qs.filter(id__lte=200)
        return qs 
    list_display = ['insert_time', 'update_time', 'customer', 'sim_number',]
    search_fields = ['customer__customer_key', 'sim_number']
    readonly_fields = ['insert_time', 'update_time']
    autocomplete_fields  = ('customer',)
    list_filter = ()

admin.site.register(SimCard, SimCardAdmin)
admin.site.register(SimCardValueEstimation, SimCardValueEstimationAdmin)
