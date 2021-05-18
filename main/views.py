import pytz
from .models import Person
from django.shortcuts import render
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

                if len(_emso) != 13 or not _emso.isdigit():
                    return HttpResponse("<h3>Nepravilen EMŠO</h3>")
                elif ime.isdigit() or priimek.isdigit():
                    return HttpResponse("<h3>Nepravilno ime ali priimek</h3>")
                elif Person.objects.get(emso=_emso):
                    return render(response, "main/ze-prijavljen.html", {"datum": Person.objects.get(emso=_emso).signupDate.strftime("%d/%m/%Y %H:%M:%S")})

            except Person.DoesNotExist:
                person = Person(emso=_emso, nameInitial=ime, surnameInitial=priimek, email=_email, signupDate=datum)
                person.save()
                return render(response, "main/prijava-uspesna.html", {"email": _email, "emso": _emso, "ime": ime, "priimek": priimek, "datum": datum.strftime("%d/%m/%Y %H:%M:%S")})
            except Exception as e:
                return HttpResponse(e)

    else:
        form = VaccinationSignup()
    return render(response, "main/home.html", {"form":form})