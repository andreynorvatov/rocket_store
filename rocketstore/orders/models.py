from django.db import models
from shop.models import Product


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', null=False, blank=False)
    phone = models.CharField(max_length=12, verbose_name='Телефон', null=False, blank=False)
    email = models.EmailField(max_length=254, verbose_name='Email', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    order_number = models.CharField(max_length=6, verbose_name='Номер заказа', null=False)
    # updated = models.DateTimeField(auto_now=True)
    # paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {str(self.id)}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
