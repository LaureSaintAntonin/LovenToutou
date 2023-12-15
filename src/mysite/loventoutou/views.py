from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Bienvenue sur LovenToutou")

def user(request):
	return HttpResponse("Connectez-vous")

# Create your views here.
