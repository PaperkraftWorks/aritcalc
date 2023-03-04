from django.db import models
from operations.models import Operation
from users.models import User
import uuid

# Create your models here.
class Record(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operation=models.ForeignKey(to=Operation, on_delete=models.DO_NOTHING, null=True)
    user=models.ForeignKey(to=User, on_delete=models.DO_NOTHING, null=True)
    amount=models.BigIntegerField(null=False, default=0)
    user_balance=models.BigIntegerField(null=False, default=0)
    operation_response=models.TextField(null=True)
    date=models.DateTimeField(auto_now=True)
    