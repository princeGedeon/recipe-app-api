import time

from django.core.management import BaseCommand

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
class Command(BaseCommand):
    """Django command to wait database"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting database .....')
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (Psycopg2OpError,OperationalError):
                self.stdout.write('Database unavalaible,waiting 1 second ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database availble'))