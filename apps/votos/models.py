from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

class Voto(models.Model):
    categoria=models.ForeignKey(User, on_delete=models.CASCADE)
    votante=models.ForeignKey(User, related_name='user_votante', on_delete=models.CASCADE)
    votado=models.ForeignKey(User, related_name='user_votado', on_delete=models.CASCADE)