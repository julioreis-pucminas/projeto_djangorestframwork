from django.contrib import admin
from .models import *


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpf', 'nome', 'nascimento', 'endereco', 'email', 'tel1', 'tel2')
    list_display_links = ('id', 'nome', 'cpf')
    search_fields = ('nome', 'cpf')
    list_per_page = 20


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'tiragem', 'dt_emprestimo', 'dt_devolucao')
    list_per_page = 20


class TiragemAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'livro', 'disponivel')
    list_display_links = ('id', 'isbn')
    search_fields = ('isbn',)
    list_per_page = 10


class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'editora', 'autor', 'ano_publicacao')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(Tiragem, TiragemAdmin)
admin.site.register(Livro, LivroAdmin)
