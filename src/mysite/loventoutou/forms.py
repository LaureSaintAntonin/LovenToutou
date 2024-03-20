from django import forms
from django.forms import ModelForm
from loventoutou.models import Owner

#créer le formulaire 
class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = "__all__"
        #possible de choisir les champs en faisant une liste ["nom", "prénom"]
        #possible de faire aussi un exclude = ["is_active", "is_staff"] - mais peu utilisé 
        #--> fonctionne 
        
class ConnectForm(forms.Form):
    mail_owner = forms.EmailField()
    password = forms.CharField()