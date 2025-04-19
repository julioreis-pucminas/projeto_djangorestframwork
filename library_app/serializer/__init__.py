from rest_framework import serializers
from datetime import timedelta
from library_app.models import *


from .aluno_serializer import *
from .emprestimo_serializer import *
from .exemplares_serializer import *
from .livro_serializer import *
from .tiragem_serializer import *