from django.shortcuts import render, redirect
from .forms import RegistroParticipanteForm, ParticipanteForm
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
            return redirect(to="usuario")
       	

    return render(request, 'usuarios/participante.html', {'form':participanteForm})


def eliminar_participante(request, id):
    participante = Participantes.objects.get(id=id)
    participante.delete()
    return redirect(to="usuario")



def modificar_participante(request, id):
    participante = Participantes.objects.get(id=id)
    
    form = ParticipanteForm(instance=participante)
    data = {
        'form': form
    }
    if request.method == 'POST':
        formulario = ParticipanteForm(data=request.POST, instance=participante)

        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Modificado Correctamente."
            data['form']=formulario
            return redirect(to="usuario")
    return render(request, 'usuarios/participante.html', data)
