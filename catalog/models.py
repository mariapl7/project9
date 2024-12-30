from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)  # Наименование
    description = models.TextField(blank=True)  # Описание

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)  # Наименование
    description = models.TextField(blank=True)  # Описание
    image = models.ImageField(upload_to='products/')  # Изображение
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Категория
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена за покупку
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего изменения

    def __str__(self):
        return self.name
