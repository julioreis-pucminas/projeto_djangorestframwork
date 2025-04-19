from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from library_app.models import *
from library_app.serializer import *
from rest_framework.permissions import IsAuthenticated
from django.db.models import Prefetch


from .alunosviews import *
from .emprestimoviews import *
from .exemplaresviews import *
from .livrosviews import *
from .tiragensviews import *
from .devolucaoviews import *
from .estatisticasviews import *