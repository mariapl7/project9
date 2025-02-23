from django.core.management.base import BaseCommand
from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate


class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        post_migrate.connect(create_moderator_group, sender=self)


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


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" и назначает необходимые разрешения'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Получите разрешения, которые вы хотите назначить
        permissions = [
            'products.add_product',
            'products.change_product',
            'products.delete_product',
            # Добавьте другие разрешения по необходимости
        ]

        for perm in permissions:
            try:
                permission = get(codename=perm.split('.')[-1])
                group.permissions.add(permission)
                self.stdout.write(self.style.SUCCESS(f'Добавлено разрешение: {permission}'))
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Разрешение не найдено: {perm}'))

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана и разрешения назначены.'))
