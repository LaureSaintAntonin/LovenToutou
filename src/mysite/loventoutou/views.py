from django.shortcuts import render


def index(request): 
    return render(request, "loventoutou/index.html")

def connexion(request):
	return render(request, "loventoutou/connexion.html")

# def register(request):
#   return render(request, "loventoutou/register.html")

def user(request):
    return render(request, "loventoutou/user.html")

def navigation(request):
    return render(request, "loventoutou/navigation.html")

# Create your views here.
