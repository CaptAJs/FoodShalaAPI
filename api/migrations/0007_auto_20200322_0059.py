# Generated by Django 2.0.13 on 2020-03-22 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200322_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 0, 59, 30, 102719)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 0, 59, 30, 101850)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 0, 59, 30, 101817)),
        ),
    ]
