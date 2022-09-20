from django.db import models
from catalog.models import Product

# Create your models here.
class Order(models.Model):
    # customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField()
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,blank=True,null=True)
    date_added = models.DateField(auto_now_add=True)