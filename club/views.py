"""This is a module to determine which data will be displayed"""
import datetime
from django.shortcuts import render
from .models import Training

now = datetime.datetime.now()

def training_list(request):
    """List of trainings which will be displayed"""
    trainings = Training.objects.filter(state="A", training_date__gte=now).order_by('training_date', 'start_time')
    return render(request, 'club/training_list.html', {'trainings' : trainings})


