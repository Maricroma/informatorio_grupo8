from django.db import models
from apps.usuarios.models import Usuario, Paises, Sexo
from apps.votos.models import Categoria
# Create your models here.
class PerfilVisitante(models.Model):
    usuario = models.OneToOneField(Usuario, related_name="usuario_visitante", on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.DO_NOTHING, null=True)
    nacionalidad = models.ForeignKey(Paises, on_delete=models.DO_NOTHING, null=True)
    edad = models.IntegerField( null=True)

    def __str__(self):
        return self.usuario


class PerfilParticipante(models.Model):
    usuario = models.OneToOneField(Usuario, related_name="usuario_participante", on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True)
    directo = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.usuario.username

class Participantes(models.Model):
    grupoParticipante =  models.ForeignKey(PerfilParticipante, related_name="participante", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    sexo = models.ForeignKey(Sexo, on_delete=models.DO_NOTHING, null=True)
    dni = models.IntegerField()
    nacionalidad= models.ForeignKey(Paises, on_delete=models.DO_NOTHING, null=True)
    domicilio = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
