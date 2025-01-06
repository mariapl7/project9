from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        # Удаление всех существующих продуктов и категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание категорий
        category1 = Category.objects.create(name='Electronics')
        category2 = Category.objects.create(name='Clothing')
        category3 = Category.objects.create(name='Books')

        # Создание тестовых продуктов
        Product.objects.create(name='Smartphone', price=699.99, category=category1)
        Product.objects.create(name='Laptop', price=999.99, category=category1)
        Product.objects.create(name='T-shirt', price=19.99, category=category2)
        Product.objects.create(name='Novel', price=14.99, category=category3)

        self.stdout.write(self.style.SUCCESS('Successfully added test products'))