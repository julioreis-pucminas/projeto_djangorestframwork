# from rest_framework.response import Response
# from rest_framework import viewsets, status
# from library_app.models import *
# from library_app.serializer import *


# class AlunosViewSet(viewsets.ModelViewSet):
#     """Exibindo todos os alunos"""
#     queryset = Aluno.objects.all()
#     serializer_class = AlunoSerializer


# class LivrosViewSet(viewsets.ModelViewSet):
#     """Exibindo todos os alunos"""
#     queryset = Livro.objects.all()
#     serializer_class = LivroSerializer


# class TiragensViewSet(viewsets.ModelViewSet):
#     """Exibindo todos os alunos"""
#     queryset = Tiragem.objects.all()
#     serializer_class = TiragemSerializer


# class EmprestimoViewSet(viewsets.ModelViewSet):
#     queryset = Emprestimo.objects.all()
#     serializer_class = EmprestimoSerializer
#
#     def create(self, request, *args, **kwargs):
#         """Valida antes de salvar"""
#         serializer = self.get_serializer(data=request.data)
#
#         # Se os dados não forem válidos, retorna erro antes de salvar
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         tiragem = serializer.validated_data["tiragem"]
#
#         # Verifica se a tiragem já está emprestada
#         if tiragem.disponivel is False:
#             return Response(
#                 {"mensagem": "Este livro encontra-se emprestado no momento"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         # Se passou pela validação, agora salva
#         emprestimo = serializer.save()
#         tiragem.disponivel = False
#         tiragem.save()
#
#         return Response(
#             {"mensagem": "Empréstimo cadastrado com sucesso!", "id": emprestimo.id},
#             status=status.HTTP_201_CREATED
#         )


# class ExemplaresViewSet(viewsets.ModelViewSet):
#     queryset = Livro.objects.prefetch_related('tiragens').all()
#     serializer_class = ExemplaresSerializer
