# Generated by Django 3.2.9 on 2022-01-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0034_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='whos_following',
            field=models.IntegerField(default=0),
        ),
    ]
