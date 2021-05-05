# Author: Seth Kimpler

from django.contrib import admin

from .models import GPUModel, Notification, HistoricalPrice

admin.site.register(GPUModel)
admin.site.register(Notification)
admin.site.register(HistoricalPrice)
