from urllib import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from FuncionariosApp.models import Departamento, Funcionario
from FuncionariosApp.serializers import DepartamentoSerializer, FuncionarioSerializer

# Create your views here.

@csrf_exempt
def departartamentoApi(request, id=0):
    if request.method == 'GET':
        departamentos = Departamento.objects.all()
        departamentos_serializer = DepartamentoSerializer(departamentos, many=True)
        return JsonResponse(departamentos_serializer.data, safe = False)
    
    elif request.method == 'POST':
        departamento_data = JSONParser().parse(request)
        departamentos_serializer = DepartamentoSerializer(data=departamento_data)
        if departamentos_serializer.is_valid():
            departamentos_serializer.save()
            return JsonResponse("Salvo com sucesso", safe=False)
        return JsonResponse("Falha ao Salvar", safe=False)
    
    elif request.method == 'PUT':
        departamento_data=JSONParser().parse(request)
        departamento = Departamento.objects.get(DepartamentoId = departamento_data['DepartamentoId'])
        departamentos_serializer = DepartamentoSerializer(departamento, data=departamento_data)    
        if departamentos_serializer.is_valid():
            departamentos_serializer.update()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar", safe=False)
        
    elif request.method == 'DELETE':
        departamento = Departamento.objects.get(DepartamentoId = departamento_data['DepartamentoId'])
        departamento.delete()
        return JsonResponse("Deletado com sucesso", safe=False)
        