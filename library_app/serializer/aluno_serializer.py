from library_app.serializer import *



class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'url', 'cpf', 'nome', 'sobrenome', 'nascimento', 'endereco', 'email', 'tel1', 'tel2']
        extra_kwargs = {
            "url": {"view_name": "alunos-detail", "lookup_field": "id"}
        }

    def validate_cpf(self, cpf):
        if not cpf.isnumeric() or len(cpf) != 11:
            raise serializers.ValidationError("O cpf é formado por 11 caracteres numéricos.")
        return cpf