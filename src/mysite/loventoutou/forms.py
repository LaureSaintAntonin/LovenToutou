from django.forms import ModelForm
from loventoutou.models import Owner

#créer le formulaire 
class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ["first_name","last_name", "breeding_name","siret_number","complete_address"]