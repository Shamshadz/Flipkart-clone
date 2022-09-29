from itertools import product
from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(blank=True, null=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_items(self):
        orderItems = OrderItem.objects.all()
        total = sum([item.quantity for item in orderItems])
        return total

    @property
    def get_cart_total(self):
        orderitems = OrderItem.objects.all()
        total = sum([item.get_total for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,blank=True,null=True)
    date_added = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total