from django.contrib import admin
from django.urls import path
from . import views



urlpatterns=[
	path('participante/', views.participante, name="participante"),
	path('eliminar_participante/<int:id>', views.eliminar_participante, name="eliminar_participante"),
	path('modificar_participante/<int:id>', views.modificar_participante, name="modificar_participante"),

]