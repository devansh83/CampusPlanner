from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Campus Planner Home</h1>')

def lostandfound(request):
    return HttpResponse('<h1>Lost And Found</h1>')

def timetable(request):
    return HttpResponse('<h1>Timetable</h1>')

