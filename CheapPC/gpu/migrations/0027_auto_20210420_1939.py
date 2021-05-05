# Generated by Django 3.1.7 on 2021-04-21 00:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gpu', '0026_auto_20210420_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='model_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historicalprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 20, 19, 39, 38, 529539)),
        ),
    ]