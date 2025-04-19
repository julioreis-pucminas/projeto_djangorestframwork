from library_app.views import *
from rest_framework.response import Response
from rest_framework import mixins


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    permission_classes = (IsAuthenticated,)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"status": "Aluno cadastrado com sucesso!!!",
             "dados": serializer.data}, status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        aluno = self.get_object()
        super(AlunosViewSet, self).update(request, *args, **kwargs)
        return Response(
            {"status": f"Alteração realizada com sucesso para o aluno(a): {aluno.nome} {aluno.sobrenome}"}, status=status.HTTP_201_CREATED
        )



class ListAlunosEmprestimo(generics.ListAPIView):
    def get_queryset(self):
        queryset = Emprestimo.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    permission_classes = (IsAuthenticated,)
    serializer_class = EmprestimoSerializer
