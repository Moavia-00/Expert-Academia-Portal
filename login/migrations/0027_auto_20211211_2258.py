# Generated by Django 3.2.9 on 2021-12-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0026_alter_query_query_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='comment_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='like',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='unlike',
            field=models.IntegerField(null=True),
        ),
    ]
