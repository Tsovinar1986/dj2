from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Shoes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_shoes')
    name = models.CharField('Shoes name', max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shoe'
        verbose_name_plural = 'Shoes'

class Brand(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name='shoes brand name')
    name = models.CharField('Brand name', max_length=50)
    about = models.TextField('Brand about')
    img = models.ImageField('Brand image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'