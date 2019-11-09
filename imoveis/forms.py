from django import forms
from django.forms import ModelForm
from .models import Casa, Apartamento

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = '__all__'

class ApartamentoForm(forms.ModelForm):
    class Meta:
        model = Apartamento
        fields = '__all__'
