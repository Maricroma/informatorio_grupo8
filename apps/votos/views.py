from django.shortcuts import render
from .models import Voto

# Create your views here.
def mostrarVotos(request):

    #Esto es un select * from Voto
    votos=Voto.objects.all()
    votosContados=[]
    nombresParticipantes=[]
    for voto in votos:
        if voto.votado.username not in nombresParticipantes:
            nombresParticipantes.append(voto.votado.username)
            votosContados.append(1)
        else:
            for x in range(len(nombresParticipantes)):
                if voto.votado.username == nombresParticipantes[x]:
                    votosContados[x]+=1

    votos= []
    for x in range(len(nombresParticipantes)):
        votos.append({'participante':nombresParticipantes[x], 'votos':votosContados[x]})
        
           
    data={
        'votos' : votos
    }



    return render(request, 'votos/mostrarVotos.html', data)