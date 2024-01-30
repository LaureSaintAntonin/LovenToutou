from django.urls import path
from . import views

# La fonction path() reçoit quatre paramètres,
# dont deux sont obligatoires : route et view, et deux facultatifs : kwargs et name.
app_name = "loventoutou"
urlpatterns = [
	path("", views.index, name="index"), 
	path("connexion/", views.connexion, name="connexion"),
	path("register/", views.register, name="register"),
	path("register/profil/", views.profil, name="profil"),
	path("profil/", views.profil, name="profil"),
	path("connexion/profil/", views.profil, name="profil"),
	path("navigation/", views.navigation, name="navigation"),
]

# index, connexion, register, profil et navigation fonctionnent, ne pas modifier !