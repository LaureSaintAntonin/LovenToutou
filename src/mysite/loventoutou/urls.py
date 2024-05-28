from django.urls import path
from django.contrib.auth import views
from . import views

# La fonction path() reçoit quatre paramètres,
# dont deux sont obligatoires : route et view, et deux facultatifs : kwargs et name.
app_name = "loventoutou"
urlpatterns = [
	path("", views.index, name="index"), 
	path("login_page/", views.login_page, name="login_page"),
	path("logout/", views.logout_user, name='logout'),
	path("register/", views.register, name="register"),
	path("home/", views.home, name="home"),
	


	path("navigation/", views.navigation, name="navigation"),
]

# index, connexion, register, profil et navigation fonctionnent, ne pas modifier !