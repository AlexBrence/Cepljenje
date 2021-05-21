from django import forms
import requests
from django.core.exceptions import ValidationError

emailError ={
    "required": "To polje mora biti izpolnjeno!",
    "invalid": "Prosim vnesite veljaven e-mail naslov!"
}

class VaccinationSignup(forms.Form):
    emso = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="EMŠO", max_length=13, required=True)
    nameInitial = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="Prva črka imena", min_length= 1, max_length=1, required=True)
    surnameInitial = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="Prva črka priimka", min_length=1, max_length=1, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"style": "width:400px", "class":"form-control"}), label="E-mail", max_length=100, required=True, error_messages = emailError)

    def clean(self):
        cleaned_data = super().clean()
       # emso = cleaned_data.get("emso")
       # response = requests.get("https://www.dev.nikigre.si/UMCN/api.php?umcn=" + emso)
       # emsoValidity = response.json()
        nameInitial = cleaned_data.get("nameInitial")
        surnameInitial = cleaned_data.get("surnameInitial")

        #print({emsoValidity["Valid"]})
        #if emsoValidity["Valid"] == "False":
        #    self.add_error("emso", "Nepravilen EMŠO!")
        if nameInitial.isdigit():
            self.add_error("nameInitial", "Nedovoljen znak v imenu!")
        if surnameInitial.isdigit():
            self.add_error("surnameInitial", "Nedovoljen znak v priimku!")