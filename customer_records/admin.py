from django.contrib import admin
from customer_records.models import Doctor, Lawyer, GoldSeller

class LawyerAdmin(admin.ModelAdmin):
    search_fields = ['customerkey__contains','cellphone__contains' ]

class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['customerkey__contains','cellphone__contains' ]
    list_filter =  ('city',)

class GoldSellerAdmin(admin.ModelAdmin):
    search_fields = ['customerkey__contains','cellphone__contains' ]
    list_filter =  ('city',)

admin.site.register(Lawyer, LawyerAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(GoldSeller, GoldSellerAdmin)
