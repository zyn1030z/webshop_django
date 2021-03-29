from django.conf.urls import url
from django.urls import path

from .views import add_to_cart, view_cart, adjust_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<id>', add_to_cart, name='add_to_cart'),
    path('adjust/<id>', adjust_cart, name='adjust_cart'),
]
