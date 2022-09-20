import imp
from urllib import response
from django.shortcuts import render
from catalog.models import Product


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