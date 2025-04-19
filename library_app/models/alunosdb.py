from library_app.models import Base
from library_app.models.tiragensdb import *


class Aluno(Base):
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False)
    nome = models.CharField(null=False, max_length=100, blank=False)
    sobrenome = models.CharField(null=False, max_length=150, blank=False)
    nascimento = models.DateField(null=True)
    endereco = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250, unique=True, blank=False)
    tel1 = models.CharField(max_length=11, blank=False)
    tel2 = models.CharField(max_length=11, blank=True)
    tiragem = models.ManyToManyField(Tiragem, through='Emprestimo')

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
