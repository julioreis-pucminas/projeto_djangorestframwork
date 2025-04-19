import pytest
from model_bakery import baker
from library_app.models.alunosdb import Aluno

pytestmark = pytest.mark.django_db


def test_cadastrar_aluno():
    dados = Aluno.objects.create(cpf='09287744562', nome='julio', sobrenome='dos reis', nascimento="1980-05-18",
                                 endereco="Rua luis de barros", email="julio@yahoo.com.br", tel1="21965236547",
                                 tel2="21986359789")
    assert dados.cpf == '09287744562'
    assert dados.nome == 'julio'
    assert dados.sobrenome == 'dos reis'
    assert dados.nascimento == '1980-05-18'
    assert dados.endereco == 'Rua luis de barros'
    assert dados.email == 'julio@yahoo.com.br'
    assert dados.tel1 == '21965236547'
    assert dados.tel2 == '21986359789'

# def test_cadastrar_aluno_mommy():
#     dados = baker.make('library_app.Aluno', cpf='09287744562', nome='julio', sobrenome='dos reis',
#                        nascimento="1980-05-18", endereco="Rua luis de barros", email="julio@yahoo.com.br",
#                        tel1="21965236547", tel2="21986359789")
#     assert dados.cpf == '09287744562'
#     assert dados.nome == 'julio'
#     assert dados.sobrenome == 'dos reis'
#     assert dados.nascimento == '1980-05-18'
#     assert dados.endereco == 'Rua luis de barros'
#     assert dados.email == 'julio@yahoo.com.br'
#     assert dados.tel1 == '21965236547'
#     assert dados.tel2 == '21986359789'
