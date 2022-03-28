from django.db import models

# Create your models here.
class Departamento(models.Model):
    DepartamentoId =  models.AutoField(primary_key=True)
    DepartamentoNome = models.CharField(max_length=500)
    
class Funcionario(models.Model):
    FuncionarioId =  models.AutoField(primary_key=True)
    FuncionarioNome = models.CharField(max_length=500)
    Departamento =  models.CharField(max_length=500)
    DataDeContratacao = models.DateField()
    ArquivoFotoNome = models.CharField(max_length=500)
    