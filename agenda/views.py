from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Agenda

# Listar todos os itens da agenda
def listar_agenda(request):
    # agendas = Agenda.objects.all()
    # agendas_serializadas = [{'_id': agenda._id, 'date': agenda.date, '_idTerapeuta': agenda._idTerapeuta.id, '_idPaciente': agenda._idPaciente.id} for agenda in agendas]
    # return JsonResponse({'agenda.html': agendas_serializadas})
    return render(request, "agenda.html")

# Criar um novo item na agenda
@csrf_exempt
def criar_item_agenda(request):
    if request.method == 'POST':
        data = request.POST
        novo_item = Agenda(date=data['date'], _idTerapeuta_id=data['_idTerapeuta'], _idPaciente_id=data['_idPaciente'])
        novo_item.save()
        return JsonResponse({'message': 'Item criado com sucesso!'})
        

# Atualizar um item na agenda
@csrf_exempt
def atualizar_item_agenda(request, pk):
    item = get_object_or_404(Agenda, pk=pk)
    if request.method == 'POST':
        data = request.POST
        item.date = data['date']
        item._idTerapeuta_id = data['_idTerapeuta']
        item._idPaciente_id = data['_idPaciente']
        item.save()
        return JsonResponse({'message': 'Item atualizado com sucesso!'})

# Deletar um item da agenda
@csrf_exempt
def deletar_item_agenda(request, pk):
    item = get_object_or_404(Agenda, pk=pk)
    if request.method == 'POST':
        item.delete()
        return JsonResponse({'message': 'Item deletado com sucesso!'})