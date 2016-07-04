"""This is module to handle with forms"""
from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    """Form to post participant to db"""
    class Meta:
        """Standard class to connect form with model"""
        model = Participant
        fields = '__all__'

