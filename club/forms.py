from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    """Form to post participant to db"""
    class Meta:
        model = Participant
        fields = '__all__'
        
