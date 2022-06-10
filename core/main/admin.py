from unicodedata import category
from django.contrib import admin
from .models import Category, Product, Brand,UserCarts
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(UserCarts)