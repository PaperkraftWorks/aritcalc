from django.db import models
import uuid
from operations.constants import TYPE_CHOICES

# Create your models here.
class Operation(models.Model):

    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type=models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        unique=True
    )
    cost=models.BigIntegerField()
    def __str__(self) -> str:
        return self.type