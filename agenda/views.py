from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Consulta


def agenda(request):
    consultas = Consulta.objects.all()
    consultas_serializadas = [{'paciente': consulta.paciente.nome, 'data_consulta': consulta.data_consulta} for consulta in consultas]

    return render(request, 'agenda.html', {'consultas': consultas_serializadas})
