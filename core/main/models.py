from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

     # def get_absolute_url(self):
     #     return reverse('home')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_product_name')
    name = models.CharField('Product  name', max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Brand(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_brand_name')
    name = models.CharField('Brand name', max_length=50)
    about = models.TextField('Brand about')
    price = models.IntegerField('Brand price', null=True)
    img = models.ImageField('Brand image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
    
class Cart(models.Model):
        name = models.CharField('Cart name', max_length=100)
        numbers = models.IntegerField('Cart numbers')
        user = models.CharField('User name', max_length=100)

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Cart'
            verbose_name_plural = 'Carts'
