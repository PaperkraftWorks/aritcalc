from django.db import models
import uuid
from users.constants import STATUS_CHOICES


# Create your models here.
class User(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.EmailField(unique=True)
    status=models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="O"
        
    )