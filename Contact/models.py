from email.policy import default
from turtle import title
from django.db import models

# Create your models here.


class contact(models.Model):
    title = models.CharField(max_length=1000, default='Contact us')
    heading = models.CharField(
        max_length=1000, default='National Institute of Laboratory Medicine & Referral Centre andtraining center')
    details = models.CharField(max_length=1000)
