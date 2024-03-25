from django.shortcuts import render
from loventoutou.forms import ConnectForm
from loventoutou.forms import OwnerForm


def index(request): 
    return render(request, "loventoutou/index.html") #fonctionne

def connexion(request):
    if request.method == "POST":
        forms = ConnectForm(request.POST)
        if forms.is_valid():
            forms.save()
    else:
        forms = ConnectForm()
        
    return render(request, "loventoutou/connexion.html", {"forms": forms})

def register(request):
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
    else:            
        form = OwnerForm() 
    
    return render(request, "loventoutou/register.html", {"form": form}) #--> fonctionne et implémente bien 
# la bdd. Fichier Bdd qui note une modification dans VSC. Mais infor restent sur le formulaire. 
# A Corriger.

def profil(request):
    return render(request, "loventoutou/user.html")

def navigation(request):
    return render(request, "loventoutou/navigation.html")
# mettre des variables de gabarit { 'first_band' : bands [0]} - 
# ceci est un exemple de variable de gabarit -à adapter en fonction

