# Generated by Django 3.2.9 on 2022-09-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='download_link',
            field=models.URLField(max_length=500),
        ),
    ]
