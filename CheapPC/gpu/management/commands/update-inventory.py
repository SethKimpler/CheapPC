# Author: Seth Kimpler

from django.core.management.base import BaseCommand
import os  # necessary for exec() call, DO NOT REMOVE


class Command(BaseCommand):
    help = 'Update out.csv with scraped data'

    def handle(self, *args, **options):
        # path needs to be relative to highest level function calling it
        exec("os.system('python gpu/management/scripts/amaz.py')")
