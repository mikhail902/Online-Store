from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(phone_number = "89145401170")
        user.set_password("12345678")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()