from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class editRoom(ModelForm):
    class Meta:
        model = Room
        fields = ["capacity", "numberOfBeds", "roomType", "price", "main_image", "image_1", "image_2", "image_3", "description"]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class editBooking(ModelForm):
    class Meta:
        model = Booking
        fields = ["startDate", "endDate"]


class editDependees(ModelForm):
    class Meta:
        model = Dependees
        fields = ["booking", "name"]
