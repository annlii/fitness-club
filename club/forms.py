"""This is module to handle with forms"""
from django import forms
from .models import Participant
from django.core.exceptions import ValidationError

class ParticipantForm(forms.ModelForm):
    """Form to post participant to db"""
    class Meta:
        """Standard class to connect form with model"""
        model = Participant
        #fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'phone', 'training']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email:
            raise forms.ValidationError("Invalid email address")
        return email

