from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("ze-prijavljen/<str:emso>", views.ze_prijavljen , name="ze-prijavljen"),
    path("prijava-uspesna/<str:emso>", views.prijava_uspesna, name="prijava-uspesna"),
]