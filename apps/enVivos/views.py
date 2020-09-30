from django.shortcuts import render

# Create your views here.
from apps.perfiles.models import PerfilParticipante
from apps.votos.models import Categoria
#loggers
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('ejemplo_Log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

def lista_de_videos_en_vivo(request, id):
    participantes=None
    categoria = "todos"
    if id==0:
        participantes = PerfilParticipante.objects.all()
    else:
        participantes = PerfilParticipante.objects.filter(categoria_id=id)
        categoria = Categoria.objects.get(id = id)
        categoria = categoria.categoria
    categorias = Categoria.objects.all()

    logger.info(categorias)
    logger.info(categoria)
    logger.info(participantes)


    data={
        'participantes' : participantes,
        'categorias':categorias,
        'categoria':categoria,
    }
    return render(request, 'enVivo/videos.html', data)