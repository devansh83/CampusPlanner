from django.shortcuts import render
from .models import event
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class EventListView(LoginRequiredMixin,ListView):
    model = event
    template_name = 'plan/home.html'
    context_object_name = 'events'
    ordering = ['-date_posted']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventDetailView(DetailView):
    model = event
    

class EventCreateView(LoginRequiredMixin, CreateView):
    model = event
    fields = ['name', 'time', 'location', 'description']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = event
    fields = ['name', 'time', 'location', 'description']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False
    
class EventDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = event
    success_url = '/home'
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False