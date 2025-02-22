from django.core.management.base import BaseCommand
from django.db.migrations.loader import MigrationLoader
from django.db import connection
from schema_history.models import SchemaChange

class Command(BaseCommand):
    help = "Tracks model schema changes and saves history."
    IGNORED_MODELS = {"contenttype", "auth", "logentry", "sessions"}
    def handle(self, *args, **kwargs):
        loader = MigrationLoader(connection)  
        graph = loader.graph  

        applied_migrations = [migration for migration in graph.leaf_nodes()]
        schema_changes = []

        for migration_name in applied_migrations:
            migration = loader.get_migration(migration_name[0], migration_name[1])

            for operation in migration.operations:
                if hasattr(operation, "name"):
                    field_name = operation.name
                else:
                    field_name = "Unknown"

                model_name = getattr(operation, "model_name", "UnknownModel")

                # Skip system models
                if any(model_name.lower().startswith(ignored) for ignored in self.IGNORED_MODELS):
                    continue  

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
