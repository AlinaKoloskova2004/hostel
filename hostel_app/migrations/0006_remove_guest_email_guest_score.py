# Generated by Django 4.1.7 on 2023-05-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0005_alter_booking_checkin_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='email',
        ),
        migrations.AddField(
            model_name='guest',
            name='score',
            field=models.IntegerField(default=20, verbose_name='Номер счёта'),
        ),
    ]
