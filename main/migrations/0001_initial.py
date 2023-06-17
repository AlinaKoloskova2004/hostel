# Generated by Django 3.1 on 2020-08-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('dt_updated', models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего изменения')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['title'],
            },
        ),
    ]
