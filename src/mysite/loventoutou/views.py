from django.shortcuts import render


def index(request): 
    return render(request, "loventoutou/index.html")

def connexion(request):
	return render(request, "loventoutou/connexion.html")

def register(request):
    return render(request, "loventoutou/register.html")

def user(request):
    return render(request, "loventoutou/user.html")

def navigation(request):
    return render(request, "loventoutou/navigation.html")
# mettre des variables de gabarit { 'first_band' : bands [0]} - 
# ceci est un exemple de variable de gabarit -à adapter en fonction


# Create your views here.
