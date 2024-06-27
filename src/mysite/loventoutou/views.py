from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import OwnerForm, LoginForm


def index(request): 
    return render(request, "loventoutou/index.html") #fonctionne


def logout_user(request):
    logout(request)
    return redirect('login_page')

# Ajoutez cette fonction pour voir les backends d'authentification configurés
def print_auth_backends():
    from django.conf import settings
    print("AUTHENTICATION_BACKENDS:")
    for backend in settings.AUTHENTICATION_BACKENDS:
        print(backend)

def login_page(request):
    print_auth_backends()
    print("login_page called")  # Indique que la vue a été appelée
    if request.method == 'POST':
        print("POST request")  # Indique que la méthode de la requête est POST
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Indique que le formulaire est valide
            mail_owner = form.cleaned_data['mail_owner']
            password = form.cleaned_data['password']
            print(f"mail_owner: {mail_owner}, password: {password}")  # Affiche les données du formulaire
            user = authenticate(mail_owner=mail_owner, password=password) 
            if user is not None:
                print("User authenticated")  # Indique que l'utilisateur a été authentifié
                login(request, user)
                return redirect('home')  # Assurez-vous que 'home' est une vue nommée dans vos URLs
            else:
                print("Authentication failed")  # Indique que l'authentification a échoué
                message = 'Identifiants invalides.'
        else:
            print("Form is not valid")  # Indique que le formulaire n'est pas valide
            message = 'formulaire non valide.'
    else:
        print("GET request")  # Indique que la méthode de la requête est GET
        form = LoginForm()
        message = ''
    
    print("Rendering template")  # Indique que le template est en cours de rendu
    return render(request, 'loventoutou/login_page.html', {'form': form, 'message': message})


def register(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(mail=user.mail_owner, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home', user.id)
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
        print(f"Utilisateur authentifié: {user.mail_owner}")
        
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