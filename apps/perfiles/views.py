from django.shortcuts import render, redirect
from .forms import RegistroParticipanteForm
# Create your views here.
from .models import Participantes,PerfilParticipante

def participante(request):
    
    participanteForm=RegistroParticipanteForm()
    participanteForm = RegistroParticipanteForm(data=request.POST)
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        perfil=PerfilParticipante.objects.get(usuario_id=request.user.id)
        if participanteForm.is_valid():
            participanteForm.save(perfil.id)
            return redirect('/')
       	

    return render(request, 'usuarios/participante.html', {'form':participanteForm})