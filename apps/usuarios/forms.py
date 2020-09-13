from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.perfiles.models import PerfilParticipante, PerfilVisitante
from apps.usuarios.models import Paises, Sexo
from django.db import transaction
from datetime import datetime
from apps.votos.models import Categoria

class RegistroUsuarioForm(UserCreationForm): 
    nacionalidad = forms.ModelChoiceField(queryset=Paises.objects.all(), empty_label="Pais", widget = forms.Select(attrs={'class':'form-control'}))
    sexo = forms.ModelChoiceField(queryset=Sexo.objects.all(), empty_label="Sexo", widget = forms.Select(attrs={'class':'form-control'}))
    edad= forms.IntegerField( widget = forms.TextInput(attrs={'class':'form-control', 'type':'number'}))
    #fecha_de_nacimineto = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, datetime.now().year+1)))
   
    class Meta:
        model = Usuario
        fields = ['username', 'email','first_name', 'last_name', 'nacionalidad','sexo', 'edad','password1', 'password2'] 
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
        }
    
    @transaction.atomic
    def save(self):
        usuario = super().save(commit = False)
        usuario.participante = False
        usuario.save()
        PerfilVisitante.objects.create(usuario=usuario, sexo = self.cleaned_data.get('sexo'),
                                                        nacionalidad = self.cleaned_data.get('nacionalidad'),
                                                        edad= self.cleaned_data.get('edad'))
                                                        #fecha_de_nacimineto= self.cleaned_data.get('fecha_de_nacimineto'))

        return usuario

class RegistroGrupoForm(UserCreationForm):
    #rol = forms.CharField(widget=forms.HiddenInput())
    nombre_de_grupo = forms.CharField( widget = forms.TextInput(attrs={'class':'form-control'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Categoria", widget = forms.Select(attrs={'class':'form-control'}))
    directo = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model= Usuario
        fields = ['nombre_de_grupo', 'email','categoria', 'directo','password1', 'password2']

        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
        }
    @transaction.atomic
    def save(self):
        usuario = super().save(commit = False)
        usuario.participante = True
        usuario.username = self.cleaned_data.get('nombre_de_grupo')
        usuario.save()
        PerfilParticipante.objects.create(usuario=usuario, categoria = self.cleaned_data.get('categoria'),
                                                        directo= self.cleaned_data.get('directo'))

        return usuario
