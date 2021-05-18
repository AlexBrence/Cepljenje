from django.shortcuts import render
from .forms import VaccinationSignup
from django.http import HttpResponse

# Create your views here.

def index(response):
    if response.method == "POST":
        form = VaccinationSignup(response.POST)
    else:
        form = VaccinationSignup()

    return render(response, "main/home.html", {"form":form})