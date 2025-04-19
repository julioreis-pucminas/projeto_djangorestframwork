import pytest
from rest_framework.test import APIClient
from unittest.mock import patch
from rest_framework.permissions import AllowAny
from library_app.models.alunosdb import Aluno

pytestmark = pytest.mark.django_db


def test_cadastro_aluno():
    with patch("library_app.views.AlunosViewSet.permission_classes", [AllowAny]):
        Aluno.objects.create(cpf='09287744562', nome='julio', sobrenome='dos reis', nascimento="1980-05-18",
                             endereco="Rua luis de barros", email="julio@yahoo.com.br", tel1="21965236547",
                             tel2="21986359789")
        client = APIClient()
        response_data = client.get("/api/v1/alunos/")
        assert response_data.status_code == 200
        assert response_data.json()[0]['cpf'] == '09287744562'
        assert response_data.json()[0]['nome'] == 'julio'
        assert response_data.json()[0]['sobrenome'] == 'dos reis'
        assert response_data.json()[0]['nascimento'] == '1980-05-18'
        assert response_data.json()[0]['endereco'] == 'Rua luis de barros'
        assert response_data.json()[0]['email'] == 'julio@yahoo.com.br'
        assert response_data.json()[0]['tel1'] == '21965236547'
        assert response_data.json()[0]['tel2'] == '21986359789'
