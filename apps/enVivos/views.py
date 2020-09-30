from django.shortcuts import render

# Create your views here.
from apps.perfiles.models import PerfilParticipante
from apps.votos.models import Categoria
from apps.votos.views import Voto, Categoria
from apps.usuarios.views import Usuario
from apps.perfiles.views import PerfilParticipante
from django.http.response import HttpResponse
import json

#loggers
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('ejemplo_Log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

def lista_de_videos_en_vivo(request, id):
    usuario=request.user
    participantes=None
    categoria = "todos"
    votos=None
    votoFiltrado=[]
    if id==0:
        participantes = PerfilParticipante.objects.all()
        votos=Voto.objects.filter(votante_id = usuario.id)
        
    else:
        participantes = PerfilParticipante.objects.filter(categoria_id=id)
        categoria = Categoria.objects.get(id = id)
        categoria = categoria.categoria
        votos= Voto.objects.filter(votante_id = usuario.id, categoria_id=id)
       
    for voto in votos:
        votoFiltrado.append(voto.votado_id)
        votos=votoFiltrado
    votoFiltrado=[]
    for voto in votos:
        perfil = PerfilParticipante.objects.get(usuario_id = voto)
        votoFiltrado.append(perfil.id)

    categorias = Categoria.objects.all()
    logger.debug(votoFiltrado)
    data={
        'participantes' : participantes,
        'categorias':categorias,
        'categoria':categoria,
        'votos': votoFiltrado
    }
    return render(request, 'enVivo/videos.html', data)

