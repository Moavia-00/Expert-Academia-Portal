# Generated by Django 3.2.9 on 2022-01-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0041_checkreaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='AboutMe',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='aboutme'),
        ),
        migrations.AddField(
            model_name='demo',
            name='City',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='demo',
            name='Country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='country'),
        ),
        migrations.AddField(
            model_name='demo',
            name='Current_Education_City',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='educationcity'),
        ),
        migrations.AddField(
            model_name='demo',
            name='Current_Education_Country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='educationcountry'),
        ),
        migrations.AddField(
            model_name='demo',
            name='Current_Education_Date_From',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Current_Education_Date_From'),
        ),
        migrations.AddField(
            model_name='demo',
            name='Current_Education_Date_To',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Current_Education_Date_To'),
        ),
        migrations.AddField(
            model_name='demo',
            name='Current_Education_Place',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='current education place'),
        ),
        migrations.AddField(
            model_name='demo',
            name='DateOfBirth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='dateofbirth'),
        ),
        migrations.AddField(
            model_name='demo',
            name='Education_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='education_type'),
        ),
        migrations.AddField(
            model_name='demo',
            name='Gender',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='gender'),
        ),
        migrations.AddField(
            model_name='demo',
            name='Interest',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='interest'),
        ),
        migrations.AddField(
            model_name='demo',
            name='PhoneNo',
            field=models.IntegerField(default=0, verbose_name='phoneno'),
        ),
        migrations.AddField(
            model_name='demo',
            name='User_Type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='usertype'),
        ),
    ]
