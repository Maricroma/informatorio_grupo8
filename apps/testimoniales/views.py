# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.testimoniales.models import Comentario
from .forms import AltaComentario

class CrearComentario(LoginRequiredMixin, CreateView):
	model = Comentario
	form_class = AltaComentario
	template_name = 'testimoniales/testimonial.html'
	success_url = reverse_lazy('testimonial')

class ListarComentarios(LoginRequiredMixin, ListView):
	model = Comentario
	template_name = 'testimoniales/listar_test.html'
