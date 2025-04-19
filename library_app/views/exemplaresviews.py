from library_app.views import *


class ExemplaresViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Livro.objects.prefetch_related('tiragens').all()
    serializer_class = ExemplaresSerializer
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # livro = serializer.save()
        self.perform_create(serializer)
        return Response(
            {"status": "Livro cadastrado com sucesso!!!",
             "dados": serializer.data}, status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        livro = self.get_object()
        super(ExemplaresViewSet, self).update(request, *args, **kwargs)
        return Response(
            {"status": f"Alteração realizada com sucesso!!!",
             "livro": f"{livro.titulo}"},
            status=status.HTTP_201_CREATED
        )
