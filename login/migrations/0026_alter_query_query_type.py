# Generated by Django 3.2.9 on 2021-12-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_alter_demo_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
