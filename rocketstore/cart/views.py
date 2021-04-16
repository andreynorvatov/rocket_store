from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponseRedirect

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from orders.forms import OrderCreateForm

from rocketstore.settings import CART_SESSION_ID


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        form = OrderCreateForm(request.POST or None)
        print(f'Cart print: {cart}')
        return render(request, 'cart.html', context={'cart': cart, 'form': form})


class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = kwargs.get('id')
        product = Product.objects.get(id=product_id)
        cart.add(product=product,
                 quantity=['quantity'])
        return HttpResponseRedirect('/cart/')


class SubtractFromCartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = kwargs.get('id')
        product = Product.objects.get(id=product_id)
        cart.subtract(product=product,
                      quantity=['quantity'])
        return HttpResponseRedirect('/cart/')


class DeleteFromCartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = kwargs.get('id')
        product = Product.objects.get(id=product_id)
        cart.delete(product)
        return HttpResponseRedirect('/cart/')
