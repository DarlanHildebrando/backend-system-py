from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class UserType(models.TextChoices):
    client = 'CLIENT', 'Client'
    enterprise = 'ENTERPRISE', 'Enterprise',
    adm = 'ADM', 'Adm'

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(max_length=100, unique=True)
    user_type = models.CharField(max_length=50, choices=UserType.choices)
    aceitaTermos = models.BooleanField(default=False)
    username = models.CharField(max_length=150, null=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']