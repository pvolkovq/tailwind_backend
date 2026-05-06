from django.contrib.auth.models import AbstractUser
from django.db import models

from config.storage import upload_to

class User(AbstractUser):
    avatar = models.ImageField(upload_to=upload_to, blank=True, null=True)

