from django.shortcuts import render
from .models import Training
import datetime

now = datetime.datetime.now()

def training_list(request):
        trainings = Training.objects.filter(state = "A", date__gte = now).order_by('date','start_time')
        return render(request, 'club/training_list.html', {'trainings' : trainings})
    
        
