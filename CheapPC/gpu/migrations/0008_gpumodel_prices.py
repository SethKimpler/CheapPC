# Generated by Django 3.1.7 on 2021-04-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpu', '0007_delete_gpumodel2'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpumodel',
            name='prices',
            field=models.JSONField(default=list),
        ),
    ]
