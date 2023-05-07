from django.db.models import Q
from django.shortcuts import render

# On importe les données du model

from product.models import Products, Category

def frontpage(request):
    products = Products.objects.all()[0:8]
    return render(request, 'core/index.html', {'products': products})



# creation de compte
def signup(request):
    return render(request, 'core/signup.html')


# connexion

def login(request):
    return render(request, 'core/login.html')

def shop(request):
    categories = Category.objects.all()
    products = Products.objects.all()


# affichage en fonction de l'item cliquez affichage des produit liée à cette catégories
    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
        
    }
    return render(request, 'core/shop.html', context)
