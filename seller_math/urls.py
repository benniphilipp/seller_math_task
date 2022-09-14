
from django.conf.urls import url
from django.contrib import admin

from .views import indexView, DeatileView

urlpatterns = [
    url(r'^list/', DeatileView.as_view(), name='detail'),
    url('', indexView.as_view(), name='index'),
]