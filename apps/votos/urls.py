from django.urls import path
from .views import mostrarVotos, votar_ajax, eliminarVoto

urlpatterns = [
    path('mostrar-votos/<int:id>', mostrarVotos, name='mostrarVotos'),
    path('votar_ajax/', votar_ajax, name='votar_ajax'),
    path('eliminarVoto/<int:id>', eliminarVoto, name='eliminarVoto')


]