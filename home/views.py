from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def logout(request):
    return render(request, 'logout.html')

def logout_view(request):
    logout(request)
    url_login = reverse('login')
    return redirect(url_login)