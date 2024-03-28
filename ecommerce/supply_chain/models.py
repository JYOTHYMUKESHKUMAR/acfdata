from django.db import models
from django.utils import timezone

# Create your models here.
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255, default='Supplier')
    material_provided = models.TextField()
    packing_options =models.CharField(max_length=50, default='update', choices=[('BULK', 'BULK'), ('DRUM', 'DRUM'), ('IBC', 'IBC')])
    purchase_price_cif_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    does_price_change_per_package = models.BooleanField(default=False)
    payment_terms = models.CharField(max_length=50, default='update', choices=[('CAD', 'CAD'), ('LC', 'LC')])
    initial_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   
    lead_time_weeks = models.IntegerField()

    def __str__(self):
        return f'Supplier {self.id}'


class Project(models.Model):
    po_date = models.DateField(default=timezone.now)
    material_supplied = models.TextField()
    selling_price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    packing_options = models.CharField(max_length=255)

    def __str__(self):
        return f'Project {self.id}'