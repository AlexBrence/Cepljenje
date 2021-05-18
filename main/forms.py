from django import forms
from django.core.validators import RegexValidator

class VaccinationSignup(forms.Form):
    emso = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="EMŠO", max_length=13, required=True)
    nameInitial = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="Prva črka imena", min_length= 1, max_length=1, required=True)
    surnameInitial = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="Prva črka priimka", min_length=1, max_length=1, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"style": "width:400px", "class":"form-control"}), label="E-mail", max_length=100, required=True)
