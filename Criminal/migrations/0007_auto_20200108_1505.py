# Generated by Django 2.1.7 on 2020-01-08 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Criminal', '0006_auto_20191228_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 8, 15, 5, 4, 293018)),
        ),
    ]
