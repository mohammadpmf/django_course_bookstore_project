from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True)
    nat_id = models.CharField(max_length=10, blank=True, unique=True)
    birth_date = models.DateField(null=True,  blank=True)
