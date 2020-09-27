from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre_completo = models.CharField(max_length = 100)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre_completo
    
