# Generated by Django 2.1.7 on 2019-12-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_background_check',
            field=models.NullBooleanField(db_index=True, default=False),
        ),
    ]