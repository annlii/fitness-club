"""This is a module to determine which data will be displayed"""
import datetime
from django.views.generic import TemplateView
from .models import Training

now = datetime.datetime.now()

class HomePageView(TemplateView):
    """Home Page with list of trainings"""
    template_name = 'club/training_list.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['trainings'] = Training.objects.filter(state="A", training_date__gte=now).order_by('training_date', 'start_time')
        return context

class BookView(TemplateView):
    """Booking page"""
    template_name = 'club/book.html'


