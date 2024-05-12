from django.shortcuts import render, redirect
from .models import Agenda
from login_terapeuta.models import LoginTerapeuta
from cadastro_paciente.models import CadastroPaciente
from .forms import ConsultaForm


def agenda(request):
    consultas = Agenda.objects.all()
    terapeutas = LoginTerapeuta.objects.all()
    pacientes = CadastroPaciente.objects.all()

    if not consultas:
        consultas = []

    if not terapeutas:
        terapeutas = []

    if not pacientes:
        pacientes = []

    return render(request, 'agenda.html', {'consultas': consultas, 'terapeutas': terapeutas, 'pacientes': pacientes})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda')
    else:
        form = ConsultaForm()

    return render(request, 'criar_consulta.html', {'form': form})

def deletar_consulta(request, id_consulta):
    consulta = Agenda.objects.get(pk=id_consulta)
    consulta.delete()
    return redirect('agenda')