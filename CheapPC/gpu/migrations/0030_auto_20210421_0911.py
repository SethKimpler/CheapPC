# Generated by Django 3.1.7 on 2021-04-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpu', '0029_auto_20210421_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprice',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
