from django.db import models
from django.contrib.auth.models import User


class Paises(models.Model):
    pais=models.TextField(max_length=20)
    def getPais(self):
        return self.pais

class Sexo(models.Model):
    sexo=models.TextField()
    def getSexo(self):
        return self.sexo


class Perfil(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento=models.DateField()
    sexo=models.ForeignKey(Sexo, on_delete=models.DO_NOTHING)
    dni=models.IntegerField()
    nacionalidad= models.ForeignKey(Paises, on_delete=models.DO_NOTHING)
    """foto=models.URLField()"""

    def getUser(self):
        return self.user

    def getFecha(self):
        return self.fecha_nacimiento
    
    def getSexo(self):
        return self.sexo
    
    def getDni(self):
        return self.dni

    def getNacionalidad(self):
        return self.nacionalidad
