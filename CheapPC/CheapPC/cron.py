# Author: Seth Kimpler

# Reference for using cron
# https://pypi.org/project/django-crontab/
# https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/
from django.utils import timezone

import datetime

from ..gpu.models import populate, GPUModel, HistoricalPrice


def get_amazon_gpus():
    print('get_amazon_gpus cron job running')
    exec('./../manage.py update')
    populate()


def update_price_charts():
    print('updating price charts')
    for gpu in GPUModel.objects.all():
        HistoricalPrice(model=gpu,
                        price=gpu.price,
                        date=datetime.datetime.now(tz=timezone.utc)
                        ).save()
