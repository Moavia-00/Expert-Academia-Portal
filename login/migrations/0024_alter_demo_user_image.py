# Generated by Django 3.2.9 on 2021-12-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_alter_demo_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='User_Image',
            field=models.ImageField(null=True, upload_to='media/%y'),
        ),
    ]
