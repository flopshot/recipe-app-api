from psycopg2 import IntegrityError
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """Django command to pause app execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write("Creating Chonio Admin")

        try:
            get_user_model().objects.create_superuser(
                'chonio@admin.com',
                '00000000'
            )
            self.stdout.write(self.style.SUCCESS("Admin Chonio Created"))
        except IntegrityError:
            self.stdout.write(self.style.SUCCESS("Chonio Already Created"))
