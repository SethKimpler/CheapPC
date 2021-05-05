# Author: Seth Kimpler

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import csv
import datetime
import pandas as pd


# Model for GPU
class GPUModel(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField(default=-1)
    link = models.CharField(max_length=500, unique=True)
    image = models.CharField(max_length=500)

    class Meta:
        ordering = ['name']

    def get_hist_prices(self):
        return self.historicalprice_set.all()

    def get_hist_prices_tuple(self):
        price_set = self.get_hist_prices()
        data_frame_list = list()
        for price in price_set:
            data_frame = pd.DataFrame({'price': [price.price], 'data': [price.date]})
            data_frame_list.append(data_frame)
        dfl = pd.concat(data_frame_list)
        return dfl

    def __str__(self):
        return self.name


# stores historical prices of a GPU
class HistoricalPrice(models.Model):
    model = models.ForeignKey(GPUModel, on_delete=models.CASCADE)
    price = models.FloatField(default=-1)
    date = models.DateTimeField()  # default=datetime.datetime.now(tz=timezone.utc))
    decreased = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    '''
    def __ge__(self, other):
        return self.price >= other
    '''

    def __str__(self):
        return str(self.model.name) + ' ' + str(self.date) + ': ' + str(self.price)


class Notification(models.Model):
    gpu = models.ForeignKey(GPUModel, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return str(self.user.username) + ' -- ' + str(self.gpu.name)


# Populates the DB with data read in from <files/out.csv>
# updated 4/14/21
def populate():
    with open('gpu/files/out.csv', 'r') as file:
        line = csv.reader(file)
        for row in line:
            GPUModel.objects.get_or_create(
                link=row[0],
                name=row[1],
                price=row[2],
                image=row[3],
            )
        file.close()
