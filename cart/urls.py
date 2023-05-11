from django.urls import path
from django.contrib.auth import views

from cart.views import add_to_cart, cart, checkout

urlpatterns = [
    
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]
