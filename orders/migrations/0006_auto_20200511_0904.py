# Generated by Django 3.0.6 on 2020-05-11 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200511_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='large',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sub',
            name='small',
            field=models.FloatField(),
        ),
    ]
