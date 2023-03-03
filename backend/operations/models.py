from django.db import models

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
    id=models.UUIDField(primary_key=True)
    type=models.CharField(
        max_length=3,
        choices=type_choices,
    )
    cost=models.BigIntegerField()