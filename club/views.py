from django.shortcuts import render
from .models import Training

# Create your views here.

def training_list(request):
    
        trainings = Training.objects.filter(state = "A").order_by('day_of_week','start_time')
        """trainings = Traning"""
        return render(request, 'club/training_list.html', {'trainings' : trainings})
    
        
