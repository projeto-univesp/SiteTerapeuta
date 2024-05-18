from django.shortcuts import render, redirect
from .models import Agenda
from django.contrib.auth.models import User
from cadastro_paciente.models import CadastroPaciente
from datetime import datetime


def agenda(request):
    consultas = Agenda.objects.all().order_by('date')
    terapeutas = User.objects.all()
    pacientes = CadastroPaciente.objects.all()

    dados_consultas = []
    for agenda in consultas:
        paciente = agenda._idPaciente
        dados_consultas.append({
            'id_agenda': agenda._id,
            'date': agenda.date,
            'name': paciente.nome,
        })

    if not consultas:
        consultas = []

    if not terapeutas:
        terapeutas = []

    if not pacientes:
        pacientes = []

    return render(request, 'agenda.html', {'consultas': dados_consultas, 'terapeutas': terapeutas, 'pacientes': pacientes})

def criar_consulta(request):
    data_consulta_str = request.POST.get('date')
    data_consulta = datetime.strptime(data_consulta_str, '%Y-%m-%dT%H:%M')
    
    id_paciente = request.POST.get('_idPaciente')
    paciente = CadastroPaciente.objects.get(pk=id_paciente)
    
    nova_consulta = Agenda(date=data_consulta, _idPaciente=paciente)
    nova_consulta.save()

    return redirect('agenda')

def deletar_consulta(request, id_agenda):
    agenda = Agenda.objects.get(pk=id_agenda)
    agenda.delete()
    return redirect('agenda')