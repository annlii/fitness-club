"""URL module"""
from django.conf.urls import url
from .views import HomePageView
from .views import BookView
from .views import SuccessView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^book/(?P<training_id>\d+)/$', BookView.as_view(), name='book'),
    url(r'^success/$', SuccessView.as_view(), name='success'),
    ]
