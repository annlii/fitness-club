"""This is a module to determine which data will be displayed"""
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectMixin
from .models import Training
from .forms import ParticipantForm

class HomePageView(TemplateView):
    """Home Page with list of trainings"""
    template_name = 'club/training_list.html'

    def get_context_data(self, **kwargs):
        now = datetime.datetime.now()
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['trainings'] = Training.objects.filter(state="A", training_date__gte=now).order_by('training_date', 'start_time')
        return context

class BookView(SingleObjectMixin, TemplateView):
    """
    Booking page - getting data of trainings and
    posting data of participant to db
    """
    template_name = 'club/book.html'
    model = Training
    form_class = ParticipantForm

    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})

class SuccessView(TemplateView):
    """Page which is displayed afted submit the booking page"""
    template_name = 'club/success.html'
    
    
    


