# Generated by Django 3.1.7 on 2021-04-14 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpu', '0014_auto_20210414_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 16, 49, 23, 312365)),
        ),
    ]
