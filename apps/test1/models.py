from sre_constants import CATEGORY
from unicodedata import category
from django.db import models


class Customer(models.Model):
    
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    CATEGORY = (
        ('indoor','indoor'),
        ('out door','out door'),
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True ,choices=CATEGORY)
    description = models.TextField(max_length=1000, null=True, blank=True)
    data_created = models.DateTimeField(max_length=50, null=True, blank=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name 


class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('out of stock','out of stock'),
        ('delivered','delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True ,choices=STATUS)
    note = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.product.name)
class Tag(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name







