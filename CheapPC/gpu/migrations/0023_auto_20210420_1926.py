# Generated by Django 3.1.7 on 2021-04-21 00:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpu', '0022_auto_20210420_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='historicalprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 20, 19, 26, 55, 705315)),
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
