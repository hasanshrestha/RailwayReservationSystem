# Generated by Django 4.0 on 2022-03-31 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RailwayApp', '0007_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(null=True),
        ),
    ]
