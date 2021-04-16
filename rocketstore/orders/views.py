from django.shortcuts import render
from django.views.generic import View
from django.db import transaction
from django.http import HttpResponseRedirect

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

import random

'''def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'order.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'order.html', {'cart': cart, 'form': form})'''


class MakeOrderView(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderCreateForm(request.POST)
        print(f'FORM: {form}')
        cart = Cart(request)
        print(f'Print post: {cart}')
        if form.is_valid():
            order = form.save(commit=False)
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            order_number = random.randint(100000, 999999)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
                cart.clear()
                return HttpResponseRedirect('/cart/')
        else:
            form = OrderCreateForm(request.POST)
        return render(request, 'cart.html', context={'cart': cart, 'form': form})

