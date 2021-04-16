from django.urls import path
from .views import *
from orders.views import MakeOrderView

urlpatterns = [
    path('', CartView.as_view(), name='cart_view_url'),
    path('add-to-cart/<int:id>/', AddToCartView.as_view(), name='add_to_cart_url'),
    path('subtract-from-cart/<int:id>', SubtractFromCartView.as_view(), name='subtract_from_cart_url'),
    path('delete-from-cart/<int:id>', DeleteFromCartView.as_view(), name='delete_from_cart_url'),
    path('make-order/', MakeOrderView.as_view(), name='make_order_url')
]
