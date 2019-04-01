import uuid
from django.db import models

# Create your models here.

class Widget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=64, unique=True, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    created_by = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.display_name
