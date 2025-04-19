from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from library_app.models import *
from library_app.views import *


class EstatisticasViewSet(viewsets.ViewSet):
    """
    ViewSet para exibir estatísticas do sistema.
    """
    permission_classes = (IsAuthenticated,)
    @action(detail=False, methods=['get'])
    def totais(self, request):
        """
        Retorna o total de livros e alunos cadastrados.
        """
        total_livros = Livro.objects.count()
        total_exemplares = Tiragem.objects.count()
        total_alunos = Aluno.objects.count()
        Total_disponiveis = Tiragem.objects.filter(disponivel = True).count()
        Total_indisponiveis = Tiragem.objects.filter(disponivel = False).count()

        return Response({
            "total_alunos": total_alunos,
            "total_livros": total_livros,
            "total_tiragens": total_exemplares,
            "livros_disponiveis": Total_disponiveis,
            "livros_emprestados": Total_indisponiveis
        })
