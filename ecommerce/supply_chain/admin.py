from django.contrib import admin

# Register your models here.
from .models import Supplier,Project


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'material_provided', 'purchase_price_cif_per_unit', 'does_price_change_per_package', 'payment_terms','initial_payment', 'lead_time_weeks')
    search_fields = ('supplier_name', 'material_provided')
    list_filter = ('does_price_change_per_package', 'payment_terms', 'lead_time_weeks')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('po_date', 'material_supplied', 'selling_price_per_unit', 'unit', 'packing_options')
    search_fields = ('material_supplied', 'supplier__supplier_name')
    list_filter = ('po_date', 'packing_options')


admin.site.register(Project, ProjectAdmin)

admin.site.register(Supplier, SupplierAdmin)



    
