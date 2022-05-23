from django.contrib import admin
from .models import Categoria, Contato


# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    # quais campos aparecerão na listagem
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')

    # quais campos poderão ser clicados
    list_display_links = ('id', 'nome')

    # quais campos aparecerão filtros para pesquisa
    list_filter = ('categoria',)

    # quantos registros aparecerão por página
    list_per_page = 10

    # quais campos poderão ser buscados
    search_fields = ('nome', 'sobrenome', 'telefone', 'email')

    #quais campos poderão ser editados direto na tabela
    list_editable = ('telefone', 'mostrar', 'categoria')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
