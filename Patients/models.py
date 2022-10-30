from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=70)
    mobilenumber = models.IntegerField()
    details = models.CharField(max_length=70)
