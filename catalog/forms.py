from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    forbidden_words = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if field == 'image':
                self.fields[field].widget.attrs['accept'] = 'image/png, image/jpeg'

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

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not (image.name.endswith('.jpg') or image.name.endswith('.jpeg') or image.name.endswith('.png')):
                raise forms.ValidationError("Допустимые форматы: JPEG, PNG.")
            if image.size > 5 * 1024 * 1024:  # 5 MB
                raise forms.ValidationError("Размер файла не должен превышать 5 MB.")
        return image

    def validate_forbidden_words(self, text):
        for word in self.forbidden_words:
            if word in text.lower():
                raise forms.ValidationError(f'Использование слова "{word}" запрещено.')
