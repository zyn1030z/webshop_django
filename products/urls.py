from django.conf.urls import url, include
from django.urls import path

from .views import all_products

urlpatterns = [
    path('products', all_products, name='products'),

]
