from django import forms
import requests
from main.models import Person


class VaccinationSignup(forms.ModelForm):
    emso = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="EMŠO", max_length=13, required=True)
    nameInitial = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="Prva črka imena", min_length= 1, max_length=1, required=True)
    surnameInitial = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="Prva črka priimka", min_length=1, max_length=1, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"style": "width:400px", "class":"form-control"}), label="E-mail", max_length=100, required=True)

    class Meta:
        model = Person
        fields = ["emso", "nameInitial", "surnameInitial", "email"]

    def clean(self):
        cleaned_data = super().clean()
        emso = cleaned_data.get("emso")
        response = requests.get("https://www.dev.nikigre.si/UMCN/api.php?umcn=" + emso)
        emsoValidity = response.json()
        nameInitial = cleaned_data.get("nameInitial")
        surnameInitial = cleaned_data.get("surnameInitial")

        if emsoValidity[0]["Valid"] == "False":
            self.add_error("emso", "Nepravilen EMŠO!")
        if nameInitial.isdigit():
            self.add_error("nameInitial", "Nedovoljen znak v imenu!")
        if surnameInitial.isdigit():
            self.add_error("surnameInitial", "Nedovoljen znak v priimku!")