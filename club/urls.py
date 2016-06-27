"""URL module"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.training_list, name='training_list'),
]
