from django.db import models

# Create your models here.


class Notice(models.Model):
    title = models.TextField(max_length=1000)
    date = models.DateField(max_length=500, null=True)
    notice_name = models.FileField(upload_to="files/")

    def __str__(self):
        return self.title
