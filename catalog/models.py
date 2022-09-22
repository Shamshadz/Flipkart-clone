from pickle import TRUE
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(null=True, max_length=50)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank= True)
    name = models.CharField(max_length=200, null=True)
    offer = models.CharField(null=True, blank=True, max_length= 50)
    subtitle = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True, blank= True)
    scrset = models.ImageField(null=True, blank= True)
    price = models.DecimalField(decimal_places=2, max_digits=16)

    @property
    def scrset_url(self):
        if self.scrset and hasattr(self.scrset, 'url'):
            return self.scrset.url

    def __str__(self) -> str:
        return self.name
