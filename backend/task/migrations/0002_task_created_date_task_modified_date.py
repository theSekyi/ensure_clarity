# Generated by Django 4.0.1 on 2022-01-22 22:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='task',
            name='modified_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
