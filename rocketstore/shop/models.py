from django.db import models


class Product(models.Model):
    description = models.TextField(max_length=150, verbose_name='Описание')
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(verbose_name='Изображение')
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена')

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('slug',)
