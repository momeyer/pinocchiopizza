# Generated by Django 3.0.6 on 2020-05-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0041_remove_orderitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
