# Generated by Django 3.0.6 on 2020-05-11 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20200511_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('SMALL', 'SMALL'), ('LARGE', 'LARGE')], max_length=20),
        ),
    ]
