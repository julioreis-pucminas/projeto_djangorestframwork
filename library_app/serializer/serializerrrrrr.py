from rest_framework import serializers
from datetime import timedelta
from library_app.models import *


class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'url', 'cpf', 'nome', 'sobrenome', 'nascimento', 'endereco', 'email', 'tel1', 'tel2']
        extra_kwargs = {
            "url": {"view_name": "alunos-detail", "lookup_field": "id"}
        }

    def validate_cpf(self, cpf):
        if not cpf.isnumeric() or len(cpf) != 11:
            raise serializers.ValidationError("O cpf é formado por 11 caracteres numéricos.")
        return cpf


class EmprestimoSerializer(serializers.ModelSerializer):
    nome_aluno = serializers.SerializerMethodField()
    titulo_livro = serializers.SerializerMethodField()
    isbn_livro = serializers.SerializerMethodField()
    previsao_devolucao = serializers.SerializerMethodField()

    class Meta:
        model = Emprestimo
        fields = ['id', 'aluno', 'nome_aluno', 'tiragem', 'titulo_livro', 'isbn_livro', 'dt_emprestimo',
                  'previsao_devolucao', 'dt_devolucao']
        # depth = 1

    def get_nome_aluno(self, obj):
        return f"{obj.aluno.nome} {obj.aluno.sobrenome}"

    def get_titulo_livro(self, obj):
        return obj.tiragem.livro.titulo

    def get_isbn_livro(self, obj):
        return obj.tiragem.isbn

    def get_previsao_devolucao(self, obj):
        return obj.dt_emprestimo + timedelta(days=30)


class TiragemSerializer(serializers.ModelSerializer):
    livro_titulo = serializers.SerializerMethodField()

    class Meta:
        model = Tiragem
        fields = ['id', 'url', 'isbn', 'livro', 'livro_titulo', 'disponivel']
        extra_kwargs = {
            "url": {"view_name": "copias-detail", "lookup_field": "id"}
        }

    def get_livro_titulo(self, obj):
        return obj.livro.titulo

class TiragemExemplaresSerializer(serializers.ModelSerializer):
    livro_titulo = serializers.SerializerMethodField()

    class Meta:
        model = Tiragem
        fields = ['id', 'url', 'isbn', 'livro', 'livro_titulo', 'disponivel']
        extra_kwargs = {
            "url": {"view_name": "copias-detail", "lookup_field": "id"}
        }

    def get_livro_titulo(self, obj):
        return obj.livro.titulo



class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'descricao', 'editora', 'autor', 'ano_publicacao']



class ExemplaresSerializer(serializers.HyperlinkedModelSerializer):
    tiragens = TiragemSerializer(many=True, read_only=True)
    total_exemplares = serializers.SerializerMethodField()

    class Meta:
        model = Livro
        fields = ['id', 'url', 'titulo', 'descricao', 'editora', 'autor', 'ano_publicacao', 'total_exemplares', 'tiragens']
        extra_kwargs = {
            "url": {"view_name": "livros-detail", "lookup_field": "id"}
        }

    def get_total_exemplares(self, obj):
        return obj.tiragens.count()
