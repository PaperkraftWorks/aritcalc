from django.contrib.auth.models import User
from django.db import models
from users.constants import STATUS_CHOICES


# Create your models here.
class MainUser(User):
    status=models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="O"
        
    )
