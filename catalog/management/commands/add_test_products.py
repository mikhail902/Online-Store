from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()
        category, _ = Category.objects.get_or_create(name="Конфеты",description="В наличии")
        products = [
            {
                "name": "Киндер",
                "description": "Молочный шоколад",
                "category": category,
                "price": 200,
            },
            {
                "name": "Аленка",
                "description": "Молочный шоколад",
                "category": category,
                "price": "100",
            },
            {
                "name": "M&M",
                "description": "Конфеты дражже",
                "category": category,
                "price": "150",
            },
        ]
        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully added student: {product.name}'))
        else:
            self.stdout.write(self.style.WARNING(f'Student already exists: {product.name}'))