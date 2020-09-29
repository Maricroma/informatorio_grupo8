from django.shortcuts import render
from .models import Voto, Categoria
from apps.perfiles.models import PerfilParticipante
from apps.usuarios.models import Usuario
from django.http.response import HttpResponse
import json
import operator

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('ejemplo_Log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

# Create your views here.

#mostar votos   
def mostrarVotos(request, id):
    votos=None
    categoria = "todos"
    if id==0:
        votos = Voto.objects.all()
    else:
        votos = Voto.objects.filter(categoria_id=id)
        categoria = Categoria.objects.get(id = id)
        categoria = categoria.categoria
    categorias = Categoria.objects.all()
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
    votosOrdenados = sorted(votos, key=lambda x: x['votos'], reverse=True)
    data={
        'votos' : votosOrdenados,
        'categorias':categorias,
        'categoria':categoria,
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
    
def votar_ajax(request):
    data = request.POST #Guarda los datos recibidos por el método POST en la variable data
    id_video = data['id_video'] #Extrae del dicc data el valor con la key 'id_video'
    id_votante = data['id_usuario'] #Extrae del dicc data el valor con la key 'id_usuario'

    usuario_votante = Usuario.objects.get(id = id_votante) #obtiene de la DB una instancia del Usuario que votó con los datos del votante
    participante = PerfilParticipante.objects.get(id=id_video) #obtiene de la DB una instancia del PerfilParticipante 
    usuario_participante = Usuario.objects.get(id=participante.usuario_id) #con el id del perfil participante obtenemos una instancia del usuario en DB que participa
    respuesta = {} #se crea un dicc vacio que contendrá las respuestas a devolver al ajax

    if id_votante != usuario_participante.id:

        categoria = Categoria.objects.get(categoria=participante.categoria) #con la categoria en el perfil participante obtenemos de la DB una instancia de la categoria en la que participa el mismo

        voto = Voto()
        voto.categoria = categoria
        voto.votado = usuario_participante
        voto.votante = usuario_votante

        try:
            voto.save()
            respuesta = {'id_video': id_video, 'estado': 'ok'}
        except:
            respuesta = {'estado': 'error'}
    else:
        respuesta={'estado':'No podes votarte vos mismo!!'}

    data = json.dumps(respuesta)
    return HttpResponse(data, 'application/json')