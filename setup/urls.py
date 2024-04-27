"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from login_terapeuta.views import loginTerapeuta 
from agenda.views import listar_agenda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', listar_agenda), 
    path('teste/', loginTerapeuta),
    path('cadastro/', include('cadastro_paciente.urls')),
]




'''urlpatterns = [
    path('cadastropaciente/', CadastroPacienteListView.as_view(), name='cadastropaciente_list'),
    path('cadastropaciente/<int:pk>/', CadastroPacienteDetailView.as_view(), name='cadastropaciente_detail'),
    path('cadastropaciente/new/', CadastroPacienteCreateView.as_view(), name='cadastropaciente_create'),
    path('cadastropaciente/<int:pk>/edit/', CadastroPacienteUpdateView.as_view(), name='cadastropaciente_update'),
    path('cadastropaciente/<int:pk>/delete/', CadastroPacienteDeleteView.as_view(), name='cadastropaciente_delete'),
]'''

'''urlpatterns = [
    path("", CadastroPacienteListView.as_view()),
]'''

'''from django.urls import path
from cadastro_paciente.views import PacienteListView, PacienteDetailView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView

urlpatterns = [
    path('c/', PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('pacientes/novo/', PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/editar/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/excluir/', PacienteDeleteView.as_view(), name='paciente_delete'),
]'''

