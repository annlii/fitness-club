from django.shortcuts import render
from .models import Training
from datetime import date

def training_list(request):
        trainings = Training.objects.filter(state = "A").order_by('date','start_time')
        return render(request, 'club/training_list.html', {'trainings' : trainings})
    
        
