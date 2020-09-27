from django.urls import path
from .views import mostrarVotos, votar, votar_ajax

urlpatterns = [
    path('mostrar-votos/<int:id>', mostrarVotos, name='mostrarVotos'),
    path('votar/', votar, name='votar'),
    path('votar_ajax/', votar_ajax, name='votar_ajax')

]