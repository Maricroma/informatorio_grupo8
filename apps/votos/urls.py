from django.urls import path
from .views import mostrarVotos

urlpatterns = [
    path('mostrar-votos', mostrarVotos, name='mostrarVotos'),
]