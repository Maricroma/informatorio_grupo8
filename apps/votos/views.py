from django.shortcuts import render
from .models import Voto
from django.http.response import HttpResponse
# Create your views here.

#mostar votos
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

#votar

def votar(request):

    if request.method == 'POST' and request.is_ajax:
        msg = "The operation  has been recived  correctly "+request.POST
        print(request.POST)
    else:
        msg = "GET petitions are not allowed for tis view"

    return HttpResponse(msg)
    
