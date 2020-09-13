from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistroUsuarioForm, RegistroGrupoForm
from .models import Usuario
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

#imports para la clase
from django.views.generic import  CreateView
from .forms import RegistroUsuarioForm



class RegistroUsuario(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')
    


@login_required
def usuario(request):
     # Si estamos identificados devolvemos la portada  
    if request.user.is_authenticated:
        return render(request, "usuarios/user.html")
    # En otro caso redireccionamos 
    return redirect(to="login")

class RegistroParticipante(CreateView):
    model = Usuario
    form_class = RegistroGrupoForm
    template_name = 'usuarios/registro_participante.html'
    success_url = reverse_lazy('login')
