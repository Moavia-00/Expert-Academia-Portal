# Generated by Django 3.2.9 on 2022-01-24 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0047_alter_demo_dateofbirth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.query')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.demo')),
            ],
        ),
    ]
