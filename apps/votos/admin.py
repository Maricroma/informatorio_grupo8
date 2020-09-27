from django.contrib import admin
from .models import Voto, Categoria
# Register your models here.

class VotoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'votante', 'votado')
    search_fields = ('votante', 'votado') #buscar por votante o votado
    list_filter = ('categoria',) #filtrar por categoria
    list_per_page = 10


admin.site.register(Voto, VotoAdmin)
admin.site.register(Categoria)
