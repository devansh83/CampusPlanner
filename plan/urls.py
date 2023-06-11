from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='plan-home'),
    path('lostandfound', views.lostandfound, name='plan-lostandfound'),
    path('timetable', views.timetable, name='plan-timetable')
]