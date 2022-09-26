from django.urls import path, include
from cart import views

urlpatterns = [
    path('cart',views.cart,name='cart'),
]