from django.urls import path, include
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product',views.productList.as_view()),
    path('display/<str:slug>',views.display,name='display'),
]