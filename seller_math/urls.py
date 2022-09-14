
from django.conf.urls import url
from django.contrib import admin

from .views import indexView

urlpatterns = [
    url('', indexView.as_view(), name='index'),
]