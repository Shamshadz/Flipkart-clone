import imp
from multiprocessing import context
from urllib import response
from django.shortcuts import render, HttpResponse
from catalog.models import Product
import json


# for rest api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from catalog.serializers import ProductSerializer

## creating def for api call

class productList(APIView):

    def post(self, request):
        pass

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

# Create your views here.
def index(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'catalog/catalog.html', context)

def display(request,slug):
    
    product = Product.objects.filter(id=slug)

    print(product)
    context = {'product': product}

    return render(request, 'catalog/DisPro.html', context)

# def display(request):
#     id = request.POST.get('id') #['id']
#     product = Product.objects.filter(id=id)

#     print(product)
#     context = {'product': product}

#     return render(request, 'catalog/DisPro.html', context)