from django.shortcuts import render
from django.http import HttpResponse

'''def loginTerapeuta(request):
    return HttpResponse("Login!!!!")
'''

def loginTerapeuta(request):
    return render(request, "login_terapeuta/teste.html")