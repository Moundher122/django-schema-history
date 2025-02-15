from django.core.management.base import BaseCommand
from django.db.migrations.loader import MigrationLoader
from django.db import connection
from schema_history.models import SchemaChange
import json

class Command(BaseCommand):
    help = "Tracks model schema changes and saves history."
    
    def handle(self, *args, **kwargs):
        pass