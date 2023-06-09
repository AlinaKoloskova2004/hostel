# Generated by Django 4.1.7 on 2023-04-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_no',
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(default=2, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='img',
            field=models.ImageField(default=1, upload_to='%Y/%m/%d/', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=0, max_length=128, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
