from django.urls import path
from .views import homePaciente, salvar, editar, atualizar, deletar, pagina_cadastrar, listar, buscar
urlpatterns = [
    path('', homePaciente, name='homePaciente'),
    path('listar/', listar, name="listar"),
    #path('listar/', listar.as_view(), name='listar'),
    path('buscar/', buscar, name="buscar"),
    path('cadastrar/', pagina_cadastrar, name="pagina_cadastrar"),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:idPaciente>', editar, name="editar"),
    path('update/<int:idPaciente>', atualizar, name="atualizar"),
    path('deletar/<int:idPaciente>', deletar, name="deletar")
]
