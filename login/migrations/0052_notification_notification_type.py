# Generated by Django 3.2.9 on 2022-01-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0051_notification_notification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
