from django.contrib import admin
from .models import PostMap, GnafBuildings, GnafUnits, AmlakRent, AmlakSale, MaskanValueEstimation

class PostalAdmin(admin.ModelAdmin):
    fields = ('postalcode', 'city', 'neighborhood', 'average_price')
    list_display = ['postalcode', 'city', 'neighborhood']
    search_fields = ['postalcode__contains','city', 'neighborhood__contains' ]
    list_filter =  ('city',)
    readonly_fields = ['insert_time','update_time']

class GnafBuildingsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not self.get_preserved_filters(request): # if no filster or search, added by fara
            return qs.filter(buildingid__lte=200)
        return qs    
    list_display = ['buildingid', 'state_name', 'locationtype','locationname']
    search_fields = ['buildingid__contains' ]
    list_filter = ('locationtype',)

class GnafunitsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not self.get_preserved_filters(request): # if no filster or search, added by fara
            return qs.filter(id__lte=200)
        return qs    
    
    list_display = ['building', 'postalcode', 'avenue','preaventypename']
    search_fields = ['postalcode__contains' ]
    list_filter = ('preaventypename',)
    autocomplete_fields  = ( 'building',)
    list_per_page = 100

class AmlakRentAdmin(admin.ModelAdmin):
    # fields = ()
    list_display = ['postal_code', 'insert_time', 'trace_id_date','price_rahn', 'price_monthly']
    search_fields = ['postal_code__contains']
    list_filter =  ('estate_types_name',)
    readonly_fields = ['insert_time']

class AmlakSaleAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not self.get_preserved_filters(request): 
            return qs.filter(id__lte=200)
        return qs 
    list_display = ['postal_code', 'insert_time', 'trace_id_date','price']
    search_fields = ['postal_code__contains']
    list_filter =  ('estate_types_name',)
    readonly_fields = ['insert_time']

class MaskanEstimationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not self.get_preserved_filters(request): 
            return qs.filter(id__lte=200)
        return qs 
    list_display = ['customer_key', 'prediction_area', 'prediction_area_price_per_m2', 'insert_time', 'update_time']
    search_fields = ['customer_key__customer_key']
    readonly_fields = ['insert_time', 'update_time']
    autocomplete_fields  = ('customer_key',)
    list_filter = ()

admin.site.register(PostMap, PostalAdmin)
admin.site.register(GnafBuildings, GnafBuildingsAdmin)
admin.site.register(GnafUnits, GnafunitsAdmin)
admin.site.register(AmlakRent, AmlakRentAdmin)
admin.site.register(AmlakSale, AmlakSaleAdmin)
admin.site.register(MaskanValueEstimation, MaskanEstimationAdmin)
