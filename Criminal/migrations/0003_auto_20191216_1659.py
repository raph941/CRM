# Generated by Django 2.1.7 on 2019-12-16 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Criminal', '0002_crime_police'),
    ]

    operations = [
        migrations.AddField(
            model_name='crime',
            name='victim',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='crime',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 16, 59, 52, 861159)),
        ),
    ]
