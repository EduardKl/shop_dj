from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ('name',)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Алиас')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='На складе')
    available = models.BooleanField(default=True, verbose_name='Размещено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

        index_together = (('id', 'slug'),)
        ordering = ('name',)