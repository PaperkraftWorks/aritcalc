from django.db import models
from operations.models import Operation
from users.models import User

# Create your models here.
class Record(models.Model):
    id=models.UUIDField(primary_key=True)
    operation_id=models.OneToOneField(to=Operation, on_delete=models.DO_NOTHING)
    user_id=models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    amount=models.BigIntegerField(null=False, default=0)
    user_balance=models.BigIntegerField(null=False, default=0)
    operation_response=models.TextField(null=True)
    date=models.DateTimeField(auto_now=True)