from unicodedata import category
from django.shortcuts import render
from catalog.models import Product

# Create your views here.
def search(request):
    query = request.GET['query']

    if len(query) <2 or len(query) > 50:
        product = []
    else:
        product = Product.objects.filter(name__icontains=query)
        category = Product.objects.filter(category__name__icontains=query)
        product = product.union(category)
        
    context = {'product': product, 'query': query}
    return render(request, 'search/search.html', context)