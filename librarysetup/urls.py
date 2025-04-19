from django.contrib import admin
from django.urls import path, include
from library_app.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='alunos')
# router.register('api/v1/livros', LivrosViewSet, basename='Livros')
# router.register('api/v1/reservas', TiragensDisponiveisViewSet, basename='reservas')
router.register('tiragem', TiragensViewSet, basename='copias')
router.register('exemplares', ExemplaresViewSet, basename='livros')
router.register('livros/disponiveis', TiragensDisponiveisViewSet, basename='livros_disponiveis')
router.register('livros/indisponiveis', TiragensIndisponiveisViewSet, basename='livros_indisponiveis')
router.register('emprestimos', EmprestimoViewSet, basename='emprestimos')
router.register('devolucao', DevolucaoViewSet, basename='devolucao')
router.register('estatisticas', EstatisticasViewSet, basename='estatisticas')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path("admin/", admin.site.urls),
    path('aluno/<int:pk>/emprestimos/', ListAlunosEmprestimo.as_view(), name="aluno-emprestimos"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

admin.site.site_header = 'Projeto Biblioteca - Puc Minas'
admin.site.site_title = 'Puc Minas'
admin.site.index_title = 'Área Administrativa'
