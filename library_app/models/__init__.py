from django.db import models


class Base(models.Model):
    """
    Abstract Class used in other classes
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        This class makes the class Base be abstract
        """
        abstract = True


from .livrosdb import *
from .emprestimosdb import *
from .alunosdb import *
from .tiragensdb import *
