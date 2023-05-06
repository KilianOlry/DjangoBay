from django.shortcuts import render, get_object_or_404

from .models import Products

def product(request, slug):

    product = get_object_or_404(Products, slug=slug) 
    return render(request, 'product/product.html', {'product': product})
