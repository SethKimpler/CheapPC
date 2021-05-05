# Author: Seth Kimpler

from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from django.template.loader import render_to_string

# IGNORE WARNINGS - DO NOT CHANGE
from gpu.models import GPUModel, HistoricalPrice, Notification
# IGNORE WARNINGS - DO NOT CHANGE


def craft_html(notifications):
    return render_to_string('../templates/client/notification.html', {'notifications': notifications})


class Command(BaseCommand):
    help = 'type "./manage.py email-updates" to send out updates on product price drops'

    def handle(self, *args, **options):
        # loop through all users in DB
        for user in User.objects.all():

            # get all notifications linked to user
            all_notifications = Notification.objects.all().filter(user=user)

            # build up list of objects where price has dropped
            new_notifications = []
            for notif in all_notifications:
                if notif.gpu.get_hist_prices()[0].decreased:
                    new_notifications.append(notif)

            # email user list of objects with price drops
            if len(new_notifications) > 0:
                send_mail(
                    subject='New Price Drops on PCs!!!',
                    message='Here is the message.',
                    html_message=craft_html(new_notifications),
                    from_email=None,  # uses default email in CheapPC.settings
                    recipient_list=[user.email],
                    fail_silently=True,  # don't crash
                )
