from django import forms
from .models import BlogPost
from .models import Product


class ProductForm(forms.ModelForm):
    forbidden_words = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавьте ваши классы CSS
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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_forbidden_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

    def validate_forbidden_words(self, text):
        for word in self.forbidden_words:
            if word in text.lower():
                raise forms.ValidationError(f'Использование слова "{word}" запрещено.')


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview_image', 'is_published']
