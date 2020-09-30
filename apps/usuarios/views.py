from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistroUsuarioForm, RegistroGrupoForm
from .models import Usuario
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from apps.perfiles.models import PerfilParticipante, PerfilVisitante, Participantes
from apps.votos.models import Voto
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
    user= request.user
    data={}
    participantes=None
    perfil=None
    nombresGrupos=[]
    if user.is_authenticated:
        if user.participante:
            perfil=PerfilParticipante.objects.get(usuario_id=user.id)
            participantes= Participantes.objects.filter(grupoParticipante_id=perfil.id)
            data['participantes']=participantes

        else:
            perfil=PerfilVisitante.objects.get(usuario_id=user.id)
        data['perfil']=perfil
        votos = Voto.objects.filter(votante_id=user.id)
        for voto in votos:
            usuario= Usuario.objects.filter(id = voto.votado_id)
            nombre= usuario[0].username
            nombre_idVoto={'nombre':nombre, 'id_voto':voto.id}
            nombresGrupos.append(nombre_idVoto)
        data['participanteVoto']=nombresGrupos
        return render(request, "usuarios/user.html",data)
    # En otro caso redireccionamos 
    return redirect(to="login")

class RegistroParticipante(CreateView):
    model = Usuario
    form_class = RegistroGrupoForm
    template_name = 'usuarios/registro_participante.html'
    success_url = reverse_lazy('login')
