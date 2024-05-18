from django.urls import path
from .views import agenda, criar_consulta, deletar_consulta

urlpatterns = [
    path('agenda/', agenda, name='agenda'),
    path('criar_consulta/', criar_consulta, name='criar_consulta'),
    path('deletar_consulta/<int:id_consulta>/', deletar_consulta, name='deletar_consulta'),
]