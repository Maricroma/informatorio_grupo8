from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('testimoniales/', views.CrearComentario.as_view(), name='testimonial'),
	path('lista-testimoniales/', views.ListarComentarios.as_view(), name='lista_test'),
]
