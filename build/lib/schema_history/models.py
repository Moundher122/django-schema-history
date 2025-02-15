from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SchemaChange(models.Model):
    action_type = models.CharField(max_length=50, choices=[
        ('added_field', 'Added Field'),
        ('removed_field', 'Removed Field'),
        ('modified_field', 'Modified Field'),
    ])
    model_name = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_name} - {self.field_name} - {self.action_type}"
