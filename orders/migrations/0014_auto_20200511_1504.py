# Generated by Django 3.0.6 on 2020-05-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_pizza_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='base',
            field=models.CharField(choices=[('regular', 'regular'), ('SICILIAN', 'SICILIAN')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('small', 'small'), ('LARGE', 'LARGE')], max_length=20),
        ),
    ]
