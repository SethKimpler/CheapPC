# Generated by Django 3.1.7 on 2021-04-14 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpu', '0013_auto_20210414_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprice',
            name='date',
            field=models.DateTimeField(default=datetime.date(2021, 4, 14)),
        ),
        migrations.AlterField(
            model_name='historicalprice',
            name='price',
            field=models.FloatField(default=-1),
        ),
    ]