from django.shortcuts import render

# On importe les données du model

from product.models import Products

def frontpage(request):
    products = Products.objects.all()[0:8]
    return render(request, 'core/index.html', {'products': products})

def shop(request):
    products = Products.objects.all()[0:8]
    return render(request, 'core/shop.html', {'products': products})
