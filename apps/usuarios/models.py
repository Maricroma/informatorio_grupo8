from django.db import models
from django.contrib.auth.models import User


class Paises(models.Model):
    id_pais=models.IntegerField(primary_key=True)
    pais=models.TextField(max_length=20)
    def getId(self):
        return self.id_pais
    def getPais(self):
        return self.pais

class Sexo(models.Model):
    id_sexo=models.IntegerField(primary_key=True)
    sexo=models.TextField()
    def getSexo(self):
        return self.sexo
    def getId(self):
        return self.id_sexo

<<<<<<< HEAD
class CustomUserForm(UserCreationForm): 
    pass

class Perfil(models.Model):
    id_perfil=models.IntegerField(primary_key=True)
=======
class Perfil():
    id=models.IntegerField()
>>>>>>> 2aa2602d851cb2a5f6f706de128afed43f658bca
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
