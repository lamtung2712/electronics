from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(default='', max_length=200)
    slug = models.CharField(default='', max_length=200)
    descriptions = models.CharField(max_length=200)
    active = models.BooleanField(default='True')

class product(models.Model):
    title = models.CharField(default='', max_length=200)
    descriptions = models.CharField(max_length=200)
    product_img = models.CharField(max_length=200, default='')
    active = models.BooleanField(default='True')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Variation(models.Model):
    title = models.CharField(default='', max_length=200)
    price = models.IntegerField(default='')
    discount = models.IntegerField(default='')
    active = models.BooleanField(default='True')
    inventory = models.IntegerField(default=0)
    product = models.ForeignKey(product, on_delete=models.CASCADE)