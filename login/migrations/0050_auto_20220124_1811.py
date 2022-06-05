# Generated by Django 3.2.9 on 2022-01-24 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0049_notification_show_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='show_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.demo'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]