"""This is a module to determine which data will be displayed"""
import datetime
#from django.http import HttpResponseRedirect
#from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.views.generic.detail import DetailView
#from django.views.generic.edit import FormMixin
#from django.views.generic.detail import SingleObjectMixin
#from django.template.response import TemplateResponse
#from django.shortcuts import get_object_or_404
#from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Training, Booking
from .forms import BookingForm
from django.core import serializers


class HomePageView(TemplateView):
    """Home Page with list of trainings"""
    template_name = 'club/training_list.html'

    def get_context_data(self, **kwargs):
        now = datetime.datetime.now()
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['trainings'] = Training.objects.filter(state="A", training_date__gte=now).order_by('training_date', 'start_time')
        return context


class BookView(CreateView):
    """
    Booking page - getting data of chosen training and
    posting data of booked training to db and to success page
    """

    template_name = 'club/book.html'
    form_class = BookingForm
    #success_url = '/success/'

    """ 
    def post(self, request, training_id):
        form = self.form_class(request.POST)
        training = get_object_or_404(Training,pk = training_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Well done! Fitness Class has been booked for you. If you would like to cancel booked fitness class, please contact our office.')
            return HttpResponseRedirect('/book/' + training_id)
        else:
            messages.error(request, 'Oh snap! Fill/correct all fields and try submitting again.')
        return render(request, self.template_name, {'form': form, 'training': training})
       
    def get(self, request, training_id):
        training = get_object_or_404(Training,pk = training_id)
        form = self.form_class(instance=training)
        context = {'training': training,
                   'form': form}
        return render(request, self.template_name, context)
    """
    
    def get_context_data(self, **kwargs):
        context = super(BookView, self).get_context_data(**kwargs)
        context['training'] = Training.objects.get(pk=self.kwargs['training_id'])
        return context       
    """
    def form_valid(self, form):
        self.request.session['temp_data'] = serializers.serialize('json', [Booking.objects.get(id=140)])
        return super(BookView, self).form_valid(form)
    """
    
    def get_success_url(self):
        return reverse('success', args=(self.object.id,))
    
    
class SuccessView(TemplateView):
    template_name = 'club/success.html'

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['booking'] = Booking.objects.get(pk=self.kwargs['booking_id'])
        return context     


