from django.urls import path, include
from search import views

urlpatterns = [
    path('search',views.search,name='search'),
]