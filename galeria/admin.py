from django.contrib import admin
from .models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ['nome',]  ## Busca
    list_filter = ['categoria']  ## Filtro
    list_per_page = 10  ## Paginação
    list_editable = ['publicada']  ## Itens editáveis


admin.site.register(Fotografia, ListandoFotografias)