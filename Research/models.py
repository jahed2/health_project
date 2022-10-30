from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    date = models.DateField(max_length=500,null=True)
    title =  models.CharField(max_length=300)
    pdf = models.FileField(upload_to="download/")

    def __str__(self):
        return  self.title
        