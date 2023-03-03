from django.db import models
import uuid

# Create your models here.
class Operation(models.Model):
    type_choices = [
        ("ADD", "Addition"),
        ("SUB", "Subtraction"),
        ("MUL", "Multiplication"),
        ("DIV", "Division"),
        ("SQR", "Squareroot"),
        ("RDM", "Random"),
    ]
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type=models.CharField(
        max_length=3,
        choices=type_choices,
    )
    cost=models.BigIntegerField()