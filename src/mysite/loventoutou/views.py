from django.shortcuts import render
from loventoutou.forms import OwnerForm


def index(request): 
    return render(request, "loventoutou/index.html") #fonctionne

def connexion(request):
	return render(request, "loventoutou/connexion.html") #fonctionne

def register(request):
    
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #return HttpResponse("Merci de votre inscription" ou un autre template à créer)
    else:            
        form = OwnerForm
    
    
    return render(request, "loventoutou/register.html", {"form": form})

def profil(request):
    return render(request, "loventoutou/user.html")

def navigation(request):
    return render(request, "loventoutou/navigation.html")
# mettre des variables de gabarit { 'first_band' : bands [0]} - 
# ceci est un exemple de variable de gabarit -à adapter en fonction

