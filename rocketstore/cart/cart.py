from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:

    def __init__(self, request):
        """Инициализация корзины"""

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        """Добавление товара в корзину или увеличение количества товара на 1 ед."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1,
                                     'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] += 1
        self.save()
        print(f'PRINT add{self.cart[product_id]}')

    def subtract(self, product, quantity=1):
        """Умешьшение количества товара на 1 ед."""
        product_id = str(product.id)
        self.cart[product_id]['quantity'] -= 1
        self.save()
        print(f'PRINT subtract{self.cart[product_id]}')

    def delete(self, product):
        """Удаление товаров из корзины"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Перебор элементов в корзине и получение продуктов из БД"""
        product_ids = self.cart.keys()
        # получение оъектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            print(f'PRINt ITEM{item}')
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Подсчет всех товаров в корзине"""
        a = sum(item['quantity'] for item in self.cart.values())
        print(f'PRINT len {a}')
        return a

    def get_total_price(self):
        """Подсчет стоисости товаров в корзине"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def save(self):
        """Обновление сесси cart"""
        self.session[settings.CART_SESSION_ID] = self.cart
        # отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def clear(self):
        """Удаление корзины из сессии"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

