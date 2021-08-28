from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def product_detail(request):
    obj = Product.objects.get(id=1)
    context = {
        "product" : obj 
    }
    return render(request, "products/products.html", context)

def add_product(request):
    form = ProductForm(request.POST or None )
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
    'form': form,
    }     
    return render(request, 'products/product_create.html', context)
