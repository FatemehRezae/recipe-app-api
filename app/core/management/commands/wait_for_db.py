"""
Django command to wait for the database to be available
"""
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as psycopg2Error
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        db_up = False
        self.stdout.write('Waiting for database...')
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, wait a second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is ready!'))
