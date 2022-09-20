from dataclasses import fields
from rest_framework import serializers
from catalog.views import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Product
        fields = '__all__'
