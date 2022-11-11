from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
# Create your models here

class Contact(models.Model):
    name = models.CharField(max_length = 122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()
    usertype = models.CharField(max_length = 50)
    def __str__(self):
        return self.name


def time_from_now():
    return timezone.now() + timedelta(seconds=5*3600)


class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    posted = models.DateTimeField(default = timezone.now())
    deadline = models.DateTimeField(default = (timezone.now() + timedelta(seconds=5*3600)))
    late = models.CharField(default='On Time' ,max_length= 10)
    completion = models.CharField(default='Not done', max_length=20)
    user = models.ForeignKey(User , max_length=30, on_delete=models.CASCADE)
    @property
    def closed(self) -> bool:
        if (timezone.now() > self.deadline):
            self.late = "Late"
        return timezone.now() < self.deadline

    def __str__(self):
        return self.title



