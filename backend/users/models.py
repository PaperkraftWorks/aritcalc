from django.db import models

# Create your models here.
class User(models.Model):
    status_choices = [
        ("I", "Active"),
        ("O", "Inactie"),
    ]
    id=models.UUIDField(primary_key=True)
    username=models.EmailField(unique=True)
    status=models.CharField(
        max_length=1,
        choices=status_choices,
        default="O"
        
    )