# Generated by Django 3.2.9 on 2022-01-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0048_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='show_user',
            field=models.IntegerField(default=0),
        ),
    ]
