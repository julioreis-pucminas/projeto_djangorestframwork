from library_app.serializer import *
from library_app.serializer.tiragem_serializer import TiragemSerializer

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


