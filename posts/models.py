from django.db import models

# Create your models here.
class Post(models.Model):
    title =models.TextField(max_length=1000)
    cover = models.ImageField(upload_to = 'images/')
    
    def __str__(self):
        return self.title
    