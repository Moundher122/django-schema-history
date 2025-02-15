# Django Schema History

Django Schema History is a package that tracks schema changes in Django models and stores the history in the database. It helps developers monitor changes such as adding, modifying, or removing fields.

## Features
- Tracks model schema changes automatically.
- Records field additions, modifications, and deletions.
- Stores historical data in a structured format.
- Integrates seamlessly with Django's migration system.

## Installation

You can install Django Schema History using pip:

```sh
pip install django-schema-history
```

## Configuration

1. Add `schema_history` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'schema_history',
]
```

2. Run migrations:

```sh
python manage.py migrate schema_history
```

## Usage

### Running Schema Change Tracking
To track schema changes, run the following command:

```sh
python manage.py track_schema_changes
```

This will log and save schema changes into the `SchemaChange` model.

## Admin Panel Integration
To manage schema changes from the Django Admin panel, add the following to your `admin.py`:

```python
from django.contrib import admin
from schema_history.models import SchemaChange

@admin.register(SchemaChange)
class SchemaChangeAdmin(admin.ModelAdmin):
    list_display = ("action_type", "model_name", "field_name", "timestamp")
    search_fields = ("model_name", "field_name")
    list_filter = ("action_type", "timestamp")
```

## Model Structure
The package stores schema changes in the `SchemaChange` model:

```python
class SchemaChange(models.Model):
    action_type = models.CharField(max_length=50)  # e.g., added_field, removed_field
    model_name = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255)
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Author
Developed by Moundher. 🚀

