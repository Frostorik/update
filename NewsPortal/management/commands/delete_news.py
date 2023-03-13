from django.core.management.base import BaseCommand, CommandError
from News.models import Category


class Command(BaseCommand):
    help = 'Удаляет все новости из данной категории.'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str, help='Категория, из которой удаляются все новости.')

    def handle(self, *args, **options):
        category = options['category']
        confirmed = input(f'Вы уверены, что хотите удалить все новости из категории?"{category}"? (y/N): ')
        if confirmed.lower() == 'y':
            num_deleted = Category.objects.filter(category=category).delete()[0]
            self.stdout.write(self.style.SUCCESS(f'Успешно удалено {num_deleted} новости из категории "{category}"'))
        else:
            self.stdout.write(self.style.WARNING('Удаление отменено.'))
