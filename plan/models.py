from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class event(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
    
