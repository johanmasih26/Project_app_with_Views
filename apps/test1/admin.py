from django.contrib import admin
from apps.test1.models import Customer, Product, Order, Tag

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','description']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','email']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','product','status']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tag, TagAdmin)




















