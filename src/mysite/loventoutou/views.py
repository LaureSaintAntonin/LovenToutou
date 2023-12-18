from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Bienvenue sur LovenToutou")

def connexion(request):
	return HttpResponse("Connectez-vous")

def user(request):
    return HttpResponse("Votre profil")

def navigation(request):
    return HttpResponse("A vous de jouer!")

# Create your views here.
