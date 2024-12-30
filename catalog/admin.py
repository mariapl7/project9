from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Отображение id и name в списке


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # Отображение id, name, price и category в списке
    list_filter = ('category',)  # Фильтрация по категории
    search_fields = ('name', 'description')  # Поиск по полям name и description


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
