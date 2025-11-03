import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_obj, created = Phone.objects.update_or_create(
                id=int(phone['id']),
                defaults={
                    'name': phone['name'],
                    'image': phone['image'],
                    'price': float(phone['price']),
                    'release_date': datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
                    'lte_exists': phone['lte_exists'].lower() == 'true'
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Создан телефон: {phone_obj.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Обновлен телефон: {phone_obj.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Импорт завершен. Обработано {len(phones)} телефонов')
        )