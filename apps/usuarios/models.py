from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Paises(models.Model):
    pais=models.TextField(max_length=20)
    
    def __str__(self):
        return self.pais
        
class Sexo(models.Model):
    sexo=models.TextField()
    
    def __str__(self):
        return self.sexo

class Usuario(AbstractUser):
    email = models.EmailField(unique=True, max_length=80)
    participante= models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['USERNAME']    


    def __str__(self):
        return self.email

