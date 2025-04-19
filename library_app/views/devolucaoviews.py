from library_app.views import *
from rest_framework.decorators import action
from django.utils.timezone import now
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class DevolucaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Emprestimo.objects.filter(dt_devolucao = None).all()
    serializer_class = EmprestimoSerializer

    @action(detail=True, methods=['patch'], url_path='registrar')
    def atualizar_devolucao(self, request, pk=None):
        """
        Atualiza a data de devolução de um empréstimo específico.
        """
        try:
            emprestimo = get_object_or_404(Emprestimo, tiragem_id=pk, dt_devolucao__isnull=True)

            # if emprestimo.dt_devolucao is not None:
            #     return Response(
            #         {"status": "Este livro já foi devolvido."},
            #         status=status.HTTP_400_BAD_REQUEST
            #     )

            emprestimo.dt_devolucao = now()
            emprestimo.save(update_fields=['dt_devolucao'])

            tiragem = Tiragem.objects.get(pk=emprestimo.tiragem.id)
            tiragem.disponivel = True
            tiragem.save()

            return Response(
                {
                    "status": "Devolução registrada com sucesso!",
                    "data_devolucao": emprestimo.dt_devolucao
                },
                status=status.HTTP_200_OK
            )
        except Emprestimo.DoesNotExist:
            return Response({"status": "Empréstimo não encontrado"}, status=status.HTTP_404_NOT_FOUND)
