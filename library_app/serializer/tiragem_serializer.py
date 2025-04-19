from library_app.serializer import *


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
