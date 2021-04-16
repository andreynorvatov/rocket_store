from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='products_list_url')
]
