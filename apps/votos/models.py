from django.db import models
from apps.usuarios.models import Usuario


# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    
    def __str__(self):
        return self.categoria

class Voto(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    votante=models.ForeignKey(Usuario, related_name='user_votante', on_delete=models.CASCADE)
    votado=models.ForeignKey(Usuario, related_name='user_votado', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("votante", "categoria")

    def __str__(self):
        return self.categoria