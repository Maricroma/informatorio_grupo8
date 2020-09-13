from django.contrib import admin
from django.urls import path
from . import views



urlpatterns=[
	path('registrar/', views.RegistroUsuario.as_view(), name="registrar"),
	path('usuario/', views.usuario, name="usuario"),
	path('registro-participante/', views.RegistroParticipante.as_view(), name="registroParticipante")
]