from django.db import models

# Create your models here.
class Noc(models.Model):
    title =models.TextField(max_length=1000)
    date = models.DateField(max_length=500,null=True)
    noc_name = models.FileField(upload_to = "files/")
    
    def __str__(self):
        return self.title
    