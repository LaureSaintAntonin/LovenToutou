from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from loventoutou.forms import ConnectForm, OwnerForm
from loventoutou.models import Owner


def index(request): 
    return render(request, "loventoutou/index.html") #fonctionne

def connexion(request):
    if request.method == "POST":
        form = ConnectForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            user = authenticate(request, mail_owner=mail, password=password)
            if user is not None:
                login(request, user)
                return redirect('profil')  # Rediriger vers la vue du profil
    else:
        form = ConnectForm()
        
    return render(request, "loventoutou/connexion.html", {"form": form})



def register(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profil')
    else:
        form = OwnerForm()

    return render(request, 'loventoutou/register.html', {'form': form}) #fonctionne - bdd bien implémentée -

# la bdd. Fichier Bdd qui note une modification dans VSC. Mais infos restent sur le formulaire.
# A Corriger.


def profil(request):
    # Récupérer l'utilisateur connecté
    user = request.user
    #vérifier si utilisateur est connecté
    if user.is_authenticated:
        # #filtrer les données de Owner pour l'utilisateur connecté
        owner = get_object_or_404(Owner, mail_owner=user.email)
    # Passerl les objects récupérés au template pour l'affichage
        return render(request, "loventoutou/user.html", {'owner': owner})
    else:
        #redirigez l'utilisateur vers la page de connexion s'il  n'est pas connecté
        return redirect('/connexion')
    

#Le décorateur @login_required -> seuls les utilisateurs connectés peuvent accéder à cette vue.
@login_required
def edit_profile(request):
    user = request.user
    if request.method =='POST':
        form = OwnerForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profil')
    else:
        form = OwnerForm(instance=user)
        return render(request, 'loventoutou/edit_profile.html', {'form': form})



def navigation(request):
    return render(request, "loventoutou/navigation.html")
# mettre des variables de gabarit { 'first_band' : bands [0]} - 
# ceci est un exemple de variable de gabarit -à adapter en fonction