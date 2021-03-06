# Generated by Django 3.0.6 on 2020-05-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0044_remove_orderitem_relateditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
