from library_app.serializer import *


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
