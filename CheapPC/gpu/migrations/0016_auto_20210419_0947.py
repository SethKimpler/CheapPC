# Generated by Django 3.1.7 on 2021-04-19 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpu', '0015_auto_20210414_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 9, 47, 19, 583436)),
        ),
    ]
