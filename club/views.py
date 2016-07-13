"""This is a module to determine which data will be displayed"""
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View, DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Training
from .forms import BookingForm


class HomePageView(TemplateView):
    """Home Page with list of trainings"""
    template_name = 'club/training_list.html'

    def get_context_data(self, **kwargs):
        now = datetime.datetime.now()
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['trainings'] = Training.objects.filter(state="A", training_date__gte=now).order_by('training_date', 'start_time')
        return context

class BookView(SingleObjectMixin, View):
    """
    Booking page - getting data of trainings and
    posting data of participant to db
    """
    template_name = 'club/book.html'
    #model = Training
    form_class = BookingForm
   
    """
    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    """
        
    def post(self, request, training_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Well done! Fitness Class has been booked for you. If you would like to cancel booked fitness class, please contact our office.')
            return HttpResponseRedirect('/book/' + training_id)
        else:
        #Wg dokumentacji - ale to nie dziala: We call the form’s is_valid() method; if it’s not True, we go back to the template with the form.
        #This time the form is no longer empty (unbound) so the HTML form will be populated with the data previously submitted,
        #where it can be edited and corrected as required.
            form = self.form_class()
            messages.error(request, 'Oh snap! Fill all fields and try submitting again.')
            #return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})
    
    """
    def get(self, request, training_id):
        form = BookingForm()
        context = {'form': self.get_object()}
        return render(request, self.template_name, context)
        """

    def get_object(self):
        return get_object_or_404(Training,pk=self.kwargs.get("training_id"))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, self.template_name, context)
       




