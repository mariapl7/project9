from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'


class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        from django.contrib.auth.models import Group, Permission


def create_moderator_group(sender, **kwargs):
    group, created = Group.objects.get_or_create(name='Модератор продуктов')

    # Получите разрешения, которые вы хотите назначить
    permissions = [
        'products.add_product',
        'products.change_product',
        'products.delete_product',
        # Добавьте другие разрешения по необходимости
    ]

    for perm in permissions:
        permission = Permission.objects.get(codename=perm.split('.')[-1])
        group.permissions.add(permission)
