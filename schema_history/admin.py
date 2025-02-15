from django.contrib import admin
from schema_history.models import SchemaChange 

@admin.register(SchemaChange)
class SchemaChangeAdmin(admin.ModelAdmin):
    list_display = ("action_type", "model_name", "field_name", "timestamp")
    list_filter = ("action_type",)