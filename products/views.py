from django.shortcuts import render
from .models import Product

def product_detail(request):
    obj = Product.objects.get(id=1)
    context = {
        "product" : obj 
    }
    return render(request, "products/products.html", context)