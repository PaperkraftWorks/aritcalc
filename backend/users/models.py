import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from users.constants import STATUS_CHOICES


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('username not sent')
    
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.EmailField(unique=True)
    status=models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="O"
        
    )
    USERNAME_FIELD='username'
    REQUIRED_FIELS=[
    ]
    objects=UserManager()
    