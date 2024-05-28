from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import OwnerForm, LoginForm
# from .models import Owner
from .forms import forms


def index(request): 
    return render(request, "loventoutou/index.html") #fonctionne

def logout_user(request):
    logout(request)
    return redirect('login_page')

def  login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['Email'],
                password=form.cleaned_data['Password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            message = 'Identifiants invalides.'
    return render(request, 'loventoutou/login_page.html',{'form': form})



def register(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = OwnerForm()

    return render(request, 'loventoutou/register.html', context={'form': form}) #fonctionne - bdd bien implémentée -

# la bdd. Fichier Bdd qui note une modification dans VSC. Mais infos restent sur le formulaire.
# A Corriger.


# def profil(request):
#     # Récupérer l'utilisateur connecté
#     user = request.user
#     #vérifier si utilisateur est connecté
#     if user.is_authenticated:
#         # #filtrer les données de Owner pour l'utilisateur connecté
#         owner = get_object_or_404(Owner, mail_owner=user.email)
#     # Passerl les objects récupérés au template pour l'affichage
#         return render(request, "loventoutou/home.html", {'owner': owner})
#     else:
#         #redirigez l'utilisateur vers la page de connexion s'il  n'est pas connecté
#         return redirect('/login_page')
    

#Le décorateur @login_required -> seuls les utilisateurs connectés peuvent accéder à cette vue.
@login_required
def home(request):
    user = request.user
    if request.method =='POST':
        form = OwnerForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = OwnerForm(instance=user)
        return render(request, 'loventoutou/home.html', {'form': form})



def navigation(request):
    return render(request, "loventoutou/navigation.html")
# mettre des variables de gabarit { 'first_band' : bands [0]} - 
# ceci est un exemple de variable de gabarit -à adapter en fonction