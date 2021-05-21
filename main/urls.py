from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("ze-prijavljen/<int:emso>", views.ze_prijavljen , name="ze-prijavljen"),
    path("prijava-uspesna/<int:emso>", views.prijava_uspesna, name="prijava-uspesna"),
]