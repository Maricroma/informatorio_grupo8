# Create your models here.
from django.db import models

class Comentario(models.Model):
	nombre = models.CharField(max_length=80)
	email = models.EmailField()
	mensaje = models.TextField(max_length=500)
	
	def __str__(self):
		return self.nombre
