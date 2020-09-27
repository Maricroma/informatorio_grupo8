from django.contrib import admin
from .models import PerfilVisitante, PerfilParticipante, Participantes
# Register your models here.

class PerfilParticipanteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'categoria', 'directo')
    search_fields = ('usuario',) #buscar por usuario

class ParticipantesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'domicilio')
    search_fields = ('nombre', 'apellido', 'dni') #buscar por nombre, apellido o dni
    


admin.site.register(PerfilVisitante)
admin.site.register(PerfilParticipante, PerfilParticipanteAdmin)
admin.site.register(Participantes, ParticipantesAdmin)

