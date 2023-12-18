from django.shortcuts import render
#from django.http import HttpResponse
from django.template import loader



def index(request): 
    return render(request, "loventoutou/index.html")

def connexion(request):
	return render(request, "loventoutou/connexion.html")

def user(request):
    return render(request, "loventoutou/user.html")

def navigation(request):
    return render(request, "loventoutou/navigation.html")

# Create your views here.
