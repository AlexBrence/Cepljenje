from django.contrib import admin
from .models import Person
from .forms import VaccinationSignup

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    form = VaccinationSignup
    list_display = ("emso", "nameInitial", "surnameInitial", "email", "signupDate")
    search_fields = ("emso", "email",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)

admin.site.register(Person, PersonAdmin)
