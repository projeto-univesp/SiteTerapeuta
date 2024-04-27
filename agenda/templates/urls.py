from django.urls import path
from views import listar_agenda


urlpatterns = [
    path('agenda/', listar_agenda, name='listar_agenda'),
]