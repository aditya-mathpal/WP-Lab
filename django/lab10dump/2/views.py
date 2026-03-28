from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all()

    return render(request, 'index.html', {
        'products': products
    })


def add_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/product/')

    return render(request, 'add_product.html', {'form': form})  