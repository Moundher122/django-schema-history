from django.core.management.base import BaseCommand
from django.db.migrations.loader import MigrationLoader
from django.db import connection
from schema_history.models import SchemaChange
import json

class Command(BaseCommand):
    help = "Tracks model schema changes and saves history."

    def handle(self, *args, **kwargs):
        loader = MigrationLoader(connection)
        graph = loader.graph  

        applied_migrations = [migration for migration in graph.leaf_nodes()]
        schema_changes = []

        for migration_name in applied_migrations:
            # Exclude Django system migrations
            if migration_name[0].startswith("django.contrib"):
                continue

            migration = loader.get_migration(migration_name[0], migration_name[1])

            for operation in migration.operations:
                model_name = getattr(operation, "model_name", None)

                # Skip operations without a model name
                if model_name is None:
                    continue

                field_name = getattr(operation, "name", "UnknownField")

                if "AddField" in operation.__class__.__name__:
                    action = "added_field"
                elif "RemoveField" in operation.__class__.__name__:
                    action = "removed_field"
                elif "AlterField" in operation.__class__.__name__:
                    action = "modified_field"
                else:
                    continue

                schema_changes.append(SchemaChange(
                    action_type=action,
                    model_name=model_name,
                    field_name=field_name,
                ))

        if schema_changes:
            SchemaChange.objects.bulk_create(schema_changes)
            self.stdout.write(self.style.SUCCESS("Schema changes have been tracked."))
        else:
            self.stdout.write(self.style.SUCCESS("No schema changes detected."))
