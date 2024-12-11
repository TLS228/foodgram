import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Loads ingredients from a predefined CSV file'

    def handle(self, *args, **kwargs):
        # Захардкоженный путь к файлу
        file_path = 'backend/recipes/management/ingredients.csv'

        ingredients_to_create = []

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 2:
                    self.stdout.write(self.style.WARNING(
                        f'Неверный формат строки: {row}')
                    )
                    continue
                name, measurement_unit = row
                # Создаём объект для последующей массовой вставки
                ingredients_to_create.append(Ingredient(
                    name=name.strip(),
                    measurement_unit=measurement_unit.strip()
                ))

        # Массовая вставка с игнорированием конфликтов
        Ingredient.objects.bulk_create(
            ingredients_to_create,
            ignore_conflicts=True
        )

        self.stdout.write(self.style.SUCCESS(
            f'Ингредиенты успешно добавлены из файла {file_path}')
        )
