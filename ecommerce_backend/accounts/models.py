from django.db import models

# Create your models here.
# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    is_email_verified = models.BooleanField(default=False)
    def __str__(self):
        return f" Nombre : {self.username}  correo : {self.email}"
