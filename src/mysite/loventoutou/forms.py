from django import forms
from django.forms import ModelForm
from loventoutou.models import Owner

#créer le formulaire 
class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ["first_name", "last_name", "breeding_name", "siret_number", "complete_address", "phone_number", "mail_owner", "password"]
        #possible de choisir les champs en faisant une liste ["nom", "prénom"]
        #possible de faire aussi un exclude = ["is_active", "is_staff"] - mais peu utilisé 
        #--> fonctionne
        
class LoginForm(forms.Form):
    mail = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    def clean_mail(self):
        mail = self.cleaned_data.get('mail')
        if not Owner.objects.filter(mail_owner=mail).exists():
            raise forms.ValidationError("L'email n'existe pas dans la base de donnée")
        return mail