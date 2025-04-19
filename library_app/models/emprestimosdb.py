from library_app.models import Base
from library_app.models.alunosdb import *


class Emprestimo(Base):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    tiragem = models.ForeignKey(Tiragem, on_delete=models.CASCADE)
    dt_emprestimo = models.DateField()
    dt_devolucao = models.DateField(blank=True, null=True)
