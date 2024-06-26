from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import OwnerForm, LoginForm
from .forms import forms


def index(request): 
    return render(request, "loventoutou/index.html") #fonctionne


def logout_user(request):
    logout(request)
    return redirect('login_page')


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                mail_owner=form.cleaned_data['mail_owner'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            message = 'Identifiants invalides.'
    else:
        form = LoginForm()
    return render(request, 'loventoutou/login_page.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(mail=user.mail_owner, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = OwnerForm()
    return render(request, 'loventoutou/register.html',{'form': form}) #fonctionne - bdd bien implémentée -
# la bdd. Fichier Bdd qui note une modification dans VSC.

#Le décorateur @login_required -> seuls les utilisateurs connectés peuvent accéder à cette vue.
@login_required
def home(request):
    user = request.user
    if not user.is_authenticated:
        print("utilisateur non authentifié")
    else:
        print(f"Utilisateur authentifié: {user.email}")
        
    if request.method =='POST':
        print('requete POST reçue')
        form = OwnerForm(request.POST, instance=user)
        if form.is_valid():
            print('formulaire validé')
            form.save()
            return redirect('home')
        else:
            print('formulaire invalidé')
    else:
        print('requete GET reçue')
        form = OwnerForm(instance=user)
    return render(request, 'loventoutou/home.html', {'form': form})


def navigation(request):
    return render(request, "loventoutou/navigation.html")
# mettre des variables de gabarit { 'first_band' : bands [0]} - 
# ceci est un exemple de variable de gabarit -à adapter en fonction