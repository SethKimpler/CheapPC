# Generated by Django 3.1.7 on 2021-04-27 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpu', '0031_historicalprice_decrease'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalprice',
            old_name='decrease',
            new_name='decreased',
        ),
    ]
