# Author: Seth Kimpler

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Notification


# Extends Django User class
class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NotificationForm:
    class Meta:
        model = Notification
