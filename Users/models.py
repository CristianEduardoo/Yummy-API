from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField("email", unique=True)
    phone = models.IntegerField("phone", null=True, blank=True)

    USERNAME_FIELD = "email"  # Campo principal para la autenticación
    REQUIRED_FIELDS = ["username"]
