from django import forms

class VaccinationSignup(forms.Form):
    EMSO = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="EMŠO", min_length=10, max_length=10, required=True)
    nameInitial = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="Prva črka imena", min_length= 1, max_length=1, required=True)
    surnameInitial = forms.CharField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="Prva črka priimka", min_length=1, max_length=1, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={"style": "width:400px", "class":"form-control"}), label="E-mail", max_length=100, required=True)
