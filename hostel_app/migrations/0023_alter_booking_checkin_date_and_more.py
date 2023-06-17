# Generated by Django 4.1.7 on 2023-06-14 09:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0022_alter_booking_checkin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заселения'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выселения'),
        ),
    ]
