from django.shortcuts import render
from .models import event
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'plan/login.html', {'title': 'Login | Campus Planner'})

@login_required
def home(request):
    context = {
        'events': event.objects.all()
    }
    return render(request, 'plan/home.html', context)
@login_required
def lostandfound(request):
    return render(request, 'plan/lostandfound.html', {'title': 'Lost and Found'})
@login_required
def timetable(request):
    return render(request, 'plan/timetable.html', {'title': 'Timetable'})

