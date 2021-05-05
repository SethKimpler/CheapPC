# Author: Seth Kimpler

from django.core.management.base import BaseCommand
from django.utils import timezone

import datetime

# IGNORE WARNINGS - DO NOT CHANGE
from gpu.models import GPUModel, HistoricalPrice
# IGNORE WARNINGS - DO NOT CHANGE


class Command(BaseCommand):
    help = 'type "./manage.py update-historical-prices" to update historical price set'

    def handle(self, *args, **options):
        for gpu in GPUModel.objects.all():
            decreased = False
            latest_price = gpu.get_hist_prices()[0]
            if latest_price.price > gpu.price:
                decreased = True
            HistoricalPrice(model=gpu,
                            price=gpu.price,
                            date=datetime.datetime.now(tz=timezone.utc),
                            decreased=decreased
                            ).save()
