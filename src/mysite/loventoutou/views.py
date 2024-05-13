from django.shortcuts import render
from loventoutou.forms import ConnectForm
from loventoutou.forms import OwnerForm
from loventoutou.models import Owner
from django.shortcuts import redirect

def index(request): 
    return render(request, "loventoutou/index.html") #fonctionne

def connexion(request):
    if request.method == "POST":
        forms = ConnectForm(request.POST)
        if forms.is_valid():
            return redirect('/profil') # fonctionne -> page profil qui apparait bien
    else:
        forms = ConnectForm()
        
    return render(request, "loventoutou/connexion.html", {"forms": forms}) #fonctionne

def register(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profil') # fonctionne -> page profil qui apparait bien
    else:
        form = OwnerForm()

    return render(request, 'loventoutou/register.html', {'form': form}) #fonctionne - bdd bien implémentée -

# la bdd. Fichier Bdd qui note une modification dans VSC. Mais infor restent sur le formulaire.
# A Corriger.

def profil(request):
    # Récupérer toutes les entrée de l'object Owner -> Ne fonctionne pas encore
    Owners = Owner.objects.all()
    
    # Passerl les objects récupérés au template pour l'affichage
    return render(request, "loventoutou/user.html", {'owner': Owner})

def navigation(request):
    return render(request, "loventoutou/navigation.html")
# mettre des variables de gabarit { 'first_band' : bands [0]} - 
# ceci est un exemple de variable de gabarit -à adapter en fonction