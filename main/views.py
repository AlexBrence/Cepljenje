from django.urls import reverse
from .models import Person
from django.shortcuts import render
from .forms import VaccinationSignup
from django.http import HttpResponseRedirect

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
                person = Person.objects.get(emso = _emso)
                return HttpResponseRedirect(reverse("ze-prijavljen", args=[_emso]))

            except Person.DoesNotExist:
                person = Person(emso = _emso, nameInitial = ime, surnameInitial = priimek, email = _email)
                person.save()
                return HttpResponseRedirect(reverse("prijava-uspesna", args=[_emso]))
            except Exception as e:
                return HttpResponseRedirect(e)
    else:
        form = VaccinationSignup()
    return render(response, "main/home.html", {"form":form})


def ze_prijavljen(request, emso):
    p = Person.objects.get(emso=emso)
    return render(request, "main/ze-prijavljen.html", {"person": p, "date": p.signupDate.strftime("%d-%m-%Y %H:%M:%S")})


def prijava_uspesna(request, emso):
    p = Person.objects.get(emso=emso)
    return render(request, "main/prijava-uspesna.html", {"person": p, "date": p.signupDate.strftime("%d-%m-%Y %H:%M:%S")})
