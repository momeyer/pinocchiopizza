# Generated by Django 3.0.6 on 2020-05-21 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0046_auto_20200521_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PENDING', 'pending'), ('DONE', 'done'), ('PREPARING', 'preparing')], default='PENDING', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.OrderStatus'),
        ),
    ]
