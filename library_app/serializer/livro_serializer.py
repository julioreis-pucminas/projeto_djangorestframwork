from library_app.serializer import *


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'descricao', 'editora', 'autor', 'ano_publicacao']
