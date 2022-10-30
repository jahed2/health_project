# Generated by Django 3.2.9 on 2022-10-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=1000)),
                ('date', models.DateField(max_length=500, null=True)),
                ('resource_name', models.FileField(upload_to='files/')),
            ],
        ),
    ]
