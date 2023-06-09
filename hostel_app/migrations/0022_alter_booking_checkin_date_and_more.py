# Generated by Django 4.1.7 on 2023-06-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0021_alter_booking_checkin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата заселения'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата выселения'),
        ),
    ]
