import pytz
from django.db import models
from datetime import datetime

# Create your models here.


class Person(models.Model):
    emso = models.CharField(max_length=13)
    nameInitial = models.CharField(max_length=1)
    surnameInitial = models.CharField(max_length=1)
    email = models.EmailField(max_length=100)
    signupDate = models.DateTimeField(default=datetime.now())
