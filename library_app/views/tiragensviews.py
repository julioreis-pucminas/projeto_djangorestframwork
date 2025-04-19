from library_app.views import *


class TiragensViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    permission_classes = (IsAuthenticated,)
    queryset = Tiragem.objects.all()
    serializer_class = TiragemExemplaresSerializer
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # livro = serializer.save()
        self.perform_create(serializer)
        return Response(
            {"status": "Tiragem cadastrada com sucesso!!!",
             "dados": serializer.data}, status=status.HTTP_201_CREATED
        )



class TiragensDisponiveisViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    permission_classes = (IsAuthenticated,)
    queryset = Tiragem.objects.filter(disponivel=True).all()
    serializer_class = TiragemSerializer
    lookup_field = "id"


class TiragensIndisponiveisViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    permission_classes = (IsAuthenticated,)
    queryset = Tiragem.objects.filter(disponivel=False).all()
    serializer_class = TiragemSerializer