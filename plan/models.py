from django.db import models
from django.contrib.auth.models import User
class event(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
