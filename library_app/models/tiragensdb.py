from library_app.models import *
from library_app.models import Base


class Tiragem(Base):
    isbn = models.CharField(null=False, max_length=13, unique=True)
    disponivel = models.BooleanField(default=True)
    livro = models.ForeignKey(Livro, null=True, related_name="tiragens", on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.livro} - ISBN:{self.isbn} - disp:{self.disponivel}"
