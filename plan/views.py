from django.shortcuts import render
from .models import event

def login(request):
    return render(request, 'plan/login.html', {'title': 'Login | Campus Planner'})

def home(request):
    context = {
        'events': event.objects.all()
    }
    return render(request, 'plan/home.html', {'title': 'Home'}, context)

def lostandfound(request):
    return render(request, 'plan/lostandfound.html', {'title': 'Lost and Found'})

def timetable(request):
    return render(request, 'plan/timetable.html', {'title': 'Timetable'})

