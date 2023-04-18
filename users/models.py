from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=127, error_messages={"unique": "A user with that username already exists."})
    email = models.EmailField(unique=True, error_messages={"unique": "This field must be unique."})
