
from django import forms
from .models import Enfant

class PreInscription(forms.ModelForm):

    class Meta:
        model = Enfant
        fields = ('nom','prenom',)