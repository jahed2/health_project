# Generated by Django 3.2.9 on 2022-09-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOC', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noc',
            old_name='cover',
            new_name='noc_name',
        ),
        migrations.AddField(
            model_name='noc',
            name='date',
            field=models.DateField(max_length=500, null=True),
        ),
    ]
