from .forms import VaccinationSignup
from .models import Person
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    if request.method == "POST":
        form = VaccinationSignup(data=request.POST)
        if form.is_valid():
            _email = form.cleaned_data["email"]
            _emso = form.cleaned_data["emso"]
            ime = form.cleaned_data["nameInitial"].upper()
            priimek = form.cleaned_data["surnameInitial"].upper()

            try:
                person = Person.objects.get(emso = _emso)
                return HttpResponseRedirect(reverse("ze-prijavljen", args=[_emso]))

            except Person.DoesNotExist:
                person = Person(emso=_emso, nameInitial=ime, surnameInitial=priimek, email=_email)
                person.save()
                return HttpResponseRedirect(reverse("prijava-uspesna", args=[_emso]))
            except Exception as e:
                return HttpResponseRedirect(e)
    else:
        form = VaccinationSignup()
    return render(request, "main/home.html", {"form": form})


def ze_prijavljen(request, emso):
    p = Person.objects.get(emso=emso)
    return render(request, "main/ze-prijavljen.html", {"person": p})


def prijava_uspesna(request, emso):
    p = Person.objects.get(emso=emso)
    return render(request, "main/prijava-uspesna.html", {"person": p})
