# Generated by Django 3.0.6 on 2020-05-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0035_orderitem_relateditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
