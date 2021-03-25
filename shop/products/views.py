from django.shortcuts import render
from .models import Product


def index_view(request):
    return render(request, "shop/index.html")


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "products/index.html", context=context)


def product_details(request, product_id):
    cur_product = Product.objects.get(id=product_id)
    context = {
        'product': cur_product
    }
    return render(request, "products/details.html", context=context)
