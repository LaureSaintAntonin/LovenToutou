from django.http import HttpResponse


def index(request):
	return HttpResponse("Bienvenue sur LovenToutou")


def user():
	return HttpResponse("Connectez-vous")


def profil():
	return HttpResponse("Vous êtes connecté")


def navigation():
	return HttpResponse("Consulter les autres profils")

# Create your views here.
