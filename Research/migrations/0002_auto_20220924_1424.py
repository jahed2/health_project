# Generated by Django 3.2.9 on 2022-09-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumemodel',
            name='date',
            field=models.DateField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='resumemodel',
            name='title',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]
