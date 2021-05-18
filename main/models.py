from django.db import models

# Create your models here.

class Person(models.Model):
    EMSO = models.CharField(max_length=10),
    nameInitial = models.CharField(max_length=1),
    surnameInitial = models.CharField(max_length=1),
    email = models.EmailField(max_length=100),
    signupDate = models.DateTimeField()

    def __str__(self):
        return self.email