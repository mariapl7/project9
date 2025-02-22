from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


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
                permission = Permission.objects.get(codename=perm.split('.')[-1])
                group.permissions.add(permission)
                self.stdout.write(self.style.SUCCESS(f'Добавлено разрешение: {permission}'))
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Разрешение не найдено: {perm}'))

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана и разрешения назначены.'))
