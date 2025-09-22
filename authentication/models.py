from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class UserType(models.TextChoices):
    client = 'CLIENT', 'Client'
    enterprise = 'ENTERPRISE', 'Enterprise',
    adm = 'ADM', 'Adm'

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = None
    email = models.EmailField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=18, unique=True, null=True)
    user_type = models.CharField(max_length=50, choices=UserType.choices)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []