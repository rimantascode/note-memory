from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, reverse
from .models import Product
from .forms import ProductForm

def all_products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'products/all_products.html', context)

def product_detail(request, product_id):
    obj = get_object_or_404(Product, pk=product_id)
    context = {
        "products" : obj
    }
    return render(request, "products/product_detail.html", context)

def add_product(request):
    form = ProductForm(request.POST or None )
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
    'form': form,
    }     
    return render(request, 'products/product_create.html', context)

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(instance=product)
    if request.method == "POST" :
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            form = ProductForm()
            return HttpResponse("The product was updated succesfuly")
        else:
            HttpResponse("<h1>The form is not correct</h1>")
    context = {
        "product": product,
        "form": form   
    }
    return render(request, "products/edit_product.html", context)

def delete_product(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.delete
    return redirect(reverse("home"))