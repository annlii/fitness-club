"""URL module"""
from django.conf.urls import url
from .views import HomePageView
from .views import BookView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^book/(?P<pk>\d+)/$', BookView.as_view(), name='book'),
]
