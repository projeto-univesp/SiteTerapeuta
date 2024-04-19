from django.shortcuts import render, redirect
from .models import CadastroPaciente
from django.views.generic import ListView

def homePaciente(request):
    return render(request, "homePaciente.html")

#Lista todos os pacientes
def listar(request):
    paciente = CadastroPaciente.objects.all()
    return render(request, "listar.html", {"paciente": paciente})

# class listar(ListView):
#     model = CadastroPaciente
#     template_name = 'listar.html'

#confere se existe esse paciente pela busca
def buscar(request):
    if 'nome' in request.GET:
        return buscar_resultados(request)
    else:
        return render(request, 'buscar.html')
    
#busca o paciente pelo nome
def buscar_resultados(request):
    nome = request.GET['nome']
    paciente = CadastroPaciente.objects.filter(nome__icontains=nome)
    return render(request, "resultado_busca.html", {"paciente": paciente, "nome": nome})

#cadastra informações do paciente
def salvar(request):
    nome = request.POST.get("nome")
    data_nascimento = request.POST.get("data_nascimento")
    sexo = request.POST.get("sexo")
    email = request.POST.get("email")
    cpf = request.POST.get("cpf")
    rg = request.POST.get("rg")
    celular = request.POST.get("celular")
    endereco = request.POST.get("endereco")
    nacionalidade = request.POST.get("nacionalidade")
    estado_civil = request.POST.get("estadocivil")
    profissao = request.POST.get("profissao")
    convenio = request.POST.get("convenio")
    CadastroPaciente.objects.create(nome=nome, data_nascimento=data_nascimento, sexo=sexo, email=email, cpf=cpf, rg=rg, celular=celular, endereco=endereco, nacionalidade=nacionalidade, estado_civil=estado_civil, profissao=profissao, convenio=convenio)
    return redirect(homePaciente)

def pagina_cadastrar(request):
    return render(request, "cadastrar.html")

def editar(request, idPaciente):
    paciente = CadastroPaciente.objects.get(idPaciente=idPaciente)
    return render(request, "editar.html", {"paciente" : paciente})

def atualizar(request, idPaciente):
    nome = request.POST.get("nome")
    data_nascimento = request.POST.get("data_nascimento")
    sexo = request.POST.get("sexo")
    email = request.POST.get("email")
    cpf = request.POST.get("cpf")
    rg = request.POST.get("rg")
    celular = request.POST.get("celular")
    endereco = request.POST.get("endereco")
    nacionalidade = request.POST.get("nacionalidade")
    estado_civil = request.POST.get("estadocivil")
    profissao = request.POST.get("profissao")
    convenio = request.POST.get("convenio")
    paciente = CadastroPaciente.objects.get(idPaciente=idPaciente)
    paciente.nome = nome
    paciente.data_nascimento = data_nascimento
    paciente.sexo=sexo
    paciente.email=email
    paciente.cpf=cpf
    paciente.rg=rg
    paciente.celular=celular
    paciente.endereco=endereco
    paciente.nacionalidade=nacionalidade
    paciente.estado_civil=estado_civil
    paciente.profissao=profissao
    paciente.convenio=convenio
    paciente.profissao = profissao
    paciente.salvar()
    return redirect(homePaciente)

def deletar(request, idPaciente):
    paciente = CadastroPaciente.objects.get(idPaciente=idPaciente)
    paciente.delete()
    return redirect(homePaciente)
    