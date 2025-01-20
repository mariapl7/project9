from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)  # Наименование
    description = models.TextField(blank=True)  # Описание

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # Добавлено поле для изображения
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Категория
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена за покупку
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего изменения

    def __str__(self):
        return self.name


from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    forbidden_words = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']  # Добавлено поле image

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Проверка формата файла
            if not (image.name.endswith('.jpg') or image.name.endswith('.jpeg') or image.name.endswith('.png')):
                raise forms.ValidationError("Допустимые форматы: JPEG, PNG.")
            # Проверка размера файла
            if image.size > 5 * 1024 * 1024:  # 5 MB
                raise forms.ValidationError("Размер файла не должен превышать 5 MB.")
        return image

    def validate_forbidden_words(self, text):
        for word in self.forbidden_words:
            if word in text.lower():
                raise forms.ValidationError(f'Использование слова "{word}" запрещено.')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
