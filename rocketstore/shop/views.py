from django.shortcuts import render
from .models import Product

from cart.cart import Cart


def products_list(request):
    products = Product.objects.all()
    cart = Cart(request)
    return render(request, 'index.html', context={'products': products,
                                                  'cart': cart})
