# Generated by Django 3.0.6 on 2020-05-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20200512_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2)),
            ],
        ),
    ]
