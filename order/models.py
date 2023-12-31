from django.db import models
from user.models import User
from cart.models import Cart
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(default='', max_length=100)
    order_description = models.TextField(default='')
    completed = models.BooleanField(default='')

