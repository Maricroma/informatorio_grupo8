from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
class Usuario(AbstractUser):
    email = models.EmailField(unique=True, max_length=80)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['USERNAME']    


    def __str__(self):
        return self.email


class Paises(models.Model):
    pais=models.TextField(max_length=20)
    

class Sexo(models.Model):
    sexo=models.TextField()
    

class Rol(models.Model):
    rol=models.TextField(max_length=20)

class Perfil(models.Model):
    user=models.OneToOneField(Usuario, related_name="usuario_user" , on_delete=models.CASCADE)
    fecha_nacimiento=models.DateField()
    sexo=models.ForeignKey(Sexo, on_delete=models.DO_NOTHING)
    dni=models.IntegerField()
    nacionalidad= models.ForeignKey(Paises, on_delete=models.DO_NOTHING)
    rol= models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    """foto=models.URLField()"""

   
