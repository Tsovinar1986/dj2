from django.contrib import admin
from .models import Category, Shoes, Brand
# Register your models here.

admin.site.register(Category)
admin.site.register(Shoes)
admin.site.register(Brand)