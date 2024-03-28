from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone

class Supplier(models.Model):
    material_provided = models.TextField()
    packing_options = models.TextField()
    purchase_price_cif_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    does_price_change_per_package = models.BooleanField(default=False)
    payment_terms = models.CharField(max_length=50, default='update', choices=[('CAD', 'CAD'), ('LC', 'LC')])
    lead_time_weeks = models.IntegerField()

    def __str__(self):
        return f'Supplier {self.id}'

class Project(models.Model):
    po_date = models.DateField(default=timezone.now)
    material_supplied = models.TextField()
    supplier = models.CharField(max_length=255)
    selling_price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.DecimalField(max_digits=10, decimal_places=2,default=False)
    packing_options = models.CharField(max_length=255)

    def __str__(self):
        
        return f'Project {self.id}'

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('cashflow:Products_by_categories', args=[self.slug])
class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('cashflow:productdetails',args=[self.category.slug,self.slug])


