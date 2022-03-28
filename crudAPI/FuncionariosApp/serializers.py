from rest_framework import serializers
from FuncionariosApp.models import Departamento, Funcionario

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('DepartamentoId', 'DepartamentoNome')
        
class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('FuncionarioId', 'FuncionarioNome','Departamento', 'DataDeContratacao','ArquivoFotoNome')