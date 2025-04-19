from library_app.models import *
from library_app.models import Base


class Livro(Base):
    titulo = models.CharField(null=False, max_length=100)
    descricao = models.CharField(null=False, max_length=250)
    editora = models.CharField(null=False, max_length=50)
    autor = models.CharField(max_length=50)
    ano_publicacao = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo}"
