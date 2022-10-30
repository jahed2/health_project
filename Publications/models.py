from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.exceptions import ValidationError



# Create your models here.
class publication(models.Model):
    date = models.DateField(max_length=100)
    title = models.TextField(max_length=1000)
    download_link = models.FileField(upload_to ='uploads/')
    def __str__(self):
        return  self.title
        
    