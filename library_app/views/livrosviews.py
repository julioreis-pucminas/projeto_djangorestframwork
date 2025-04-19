from library_app.views import *



class LivrosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os livros"""
    permission_classes = (IsAuthenticated,)
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        livro = serializer.save()
        # self.perform_create(serializer)
        return Response(
            {"status": "Livro cadastrado com sucesso!!!",
             "dados": livro}, status=status.HTTP_201_CREATED
        )
