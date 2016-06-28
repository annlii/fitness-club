"""URL module"""
from django.conf.urls import url
from club.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
]
