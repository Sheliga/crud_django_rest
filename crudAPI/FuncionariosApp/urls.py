from django.urls import re_path
from FuncionariosApp import views

urlpatterns = [
    re_path(r'^departamento$', views.departartamentoApi),
    re_path(r'^departamento/([0-9])+', views.departartamentoApi)
]
