from django.db import models

# Create your models here.
class price(models.Model):
    
    price_list = models.FileField(upload_to="download2/")