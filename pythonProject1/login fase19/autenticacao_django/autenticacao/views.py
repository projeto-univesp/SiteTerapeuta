from django.shortcuts import render, redirect
from django.http import HttpResponse
import pyotp
import qrcode
import urllib.parse

def index(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            return redirect('login')
        elif 'cadastro' in request.POST:
            return redirect('cadastro')
    return render(request, 'autenticacao/index.html')

def login(request):
    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['senha']
        chave_mestre = "O7SP6KFFQTPBWMYR3HCSR52QXWX44CHN"

        with open('registrados.txt') as arq:
            registrados = arq.readlines()

        if any(f"{login} {senha}\n" == registro for registro in registrados):
            usuario_chave_mestre = chave_mestre + login
            link = pyotp.TOTP(usuario_chave_mestre).provisioning_uri(name=login, issuer_name="PI")
            url = urllib.parse.quote(link)

            meu_qrcode = qrcode.make(link)
            meu_qrcode.save(f"autenticacao/static/{login}_qrcode.png")

            codigo = pyotp.TOTP(chave_mestre)
            codigo_usuario = request.POST['codigo']

            if codigo.verify(codigo_usuario):
                return HttpResponse('Seja bem-vindo!!')
            else:
                return HttpResponse('Código de verificação incorreto, inicie o login novamente')

        else:
            return HttpResponse('Usuário ou senha incorretos!')
    return render(request, 'autenticacao/login.html')

def cadastro(request):
    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['senha']

        with open('registrados.txt', 'a') as arq:
            arq.write(f"{login} {senha}\n")
        return HttpResponse('Cadastro realizado com sucesso!')
    return render(request, 'autenticacao/cadastro.html')