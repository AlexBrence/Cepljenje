import pytz
from django.urls import reverse
from .models import Person
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VaccinationSignup
from datetime import datetime, timezone
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(response):
    if response.method == "POST":
        form = VaccinationSignup(response.POST)
        if form.is_valid():
            try:
                _email = form.cleaned_data["email"]
                _emso = form.cleaned_data["emso"]
                ime = form.cleaned_data["nameInitial"].upper()
                priimek = form.cleaned_data["surnameInitial"].upper()
                datum = datetime.now(pytz.timezone('Europe/Ljubljana'))
                person = Person.objects.get(emso = _emso)
                return HttpResponseRedirect(reverse("ze-prijavljen", args=[_emso]))

            except Person.DoesNotExist:
                person = Person(emso = _emso, nameInitial = ime, surnameInitial = priimek, email = _email, signupDate = datum)
                person.save()
                return HttpResponseRedirect(reverse("prijava-uspesna", args=[_emso]))
            except Exception as e:
                return HttpResponseRedirect(e)
    else:
        form = VaccinationSignup()
    return render(response, "main/home.html", {"form":form})


def ze_prijavljen(request, emso):
    p = Person.objects.get(emso=emso)
    return render(request, "main/ze-prijavljen.html", {"person": p})

def prijava_uspesna(request, emso):
    p = Person.objects.get(emso=emso)
    return render(request, "main/prijava-uspesna.html", {"person": p})
