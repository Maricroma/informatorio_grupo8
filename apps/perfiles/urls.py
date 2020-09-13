from django.contrib import admin
from django.urls import path
from . import views



urlpatterns=[
	path('participante/', views.participante, name="participante"),
]