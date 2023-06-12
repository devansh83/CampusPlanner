from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('home', EventListView.as_view(), name='plan-home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/update', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name='event-delete'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('lostandfound', views.lostandfound, name='plan-lostandfound'),
    path('timetable', views.timetable, name='plan-timetable')
]