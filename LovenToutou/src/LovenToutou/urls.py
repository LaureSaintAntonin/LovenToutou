from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
	path("user_connexion/", views.user, name="user_connexion"),
	path("profil/", views.profil, name="profil"),
	path("navigation/", views.navigation, name="navigation")
]