import time
from django.db import connections
from django.db.utils import OperationalError as DjangoDbOpsError
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OpsError


class Command(BaseCommand):
    """Django command to pause app execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except (DjangoDbOpsError, Psycopg2OpsError):
                self.stdout.write("DB unavailable, waiting one second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available"))
