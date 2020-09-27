from django.contrib import admin
from .models import Usuario, Paises, Sexo
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'participante')
    search_fields = ('email',) #buscar por email
    list_filter = ('participante',) #filtro de búsqueda: ver participantes y no participantes
    list_per_page = 10

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Paises)
admin.site.register(Sexo)
