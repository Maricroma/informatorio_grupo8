from django import forms
from apps.usuarios.models import Paises, Sexo
from.models import Participantes
from django.db import transaction
from datetime import datetime
from django import forms
from django.forms import ModelForm
from .models import PerfilParticipante


class RegistroParticipanteForm(ModelForm):
    
    sexo= forms.ModelChoiceField(queryset=Sexo.objects.all(), empty_label="Genero", widget = forms.Select(attrs={'class':'form-control'})),
    nacionalidad= forms.ModelChoiceField(queryset=Paises.objects.all(), empty_label="Pais", widget = forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Participantes
        fields = ['nombre','apellido','edad','sexo','dni','nacionalidad','domicilio'] 
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
        }
    @transaction.atomic
    def save(self, id):
        participante = super().save(commit = False)
        grupo= PerfilParticipante.objects.get(id=id)
        participante.grupoParticipante= grupo
        participante.save()

        return participante

class ParticipanteForm(ModelForm):
    sexo= forms.ModelChoiceField(queryset=Sexo.objects.all(), empty_label="Genero", widget = forms.Select(attrs={'class':'form-control'})),
    nacionalidad= forms.ModelChoiceField(queryset=Paises.objects.all(), empty_label="Pais", widget = forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Participantes
        fields = ['nombre','apellido','edad','sexo','dni','nacionalidad','domicilio'] 
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
        }