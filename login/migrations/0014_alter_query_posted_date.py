# Generated by Django 3.2.9 on 2021-12-07 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20211206_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='Posted_Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
