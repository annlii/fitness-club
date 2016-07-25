"""This is module to handle with forms"""
from django import forms
from .models import Booking
import re
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    """Form to post participant to db"""
    class Meta:
        """Standard class to connect form with model"""
        model = Booking
        fields = '__all__'
         
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            raise forms.ValidationError("Invalid email address")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r"^[0-9]*$", phone):
            raise forms.ValidationError("Invalid phone number")
        return phone

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r"^[A-Za-z]*$", first_name):
            raise forms.ValidationError("Invalid first name")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r"^[A-Za-z]*$", last_name):
            raise forms.ValidationError("Invalid last name")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email:
            raise forms.ValidationError("Invalid email address")
        return email

    
