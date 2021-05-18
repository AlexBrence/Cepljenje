from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person

# Register your models here.


class PersonAdmin(UserAdmin):
    list_display = ("emso", "nameInitial", "surnameInitial", "email", "signupDate")
    search_fields = ("emso", "email",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)


admin.site.register(Person, PersonAdmin)