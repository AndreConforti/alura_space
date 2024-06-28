from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .forms import Loginforms, CadastroForms

def login(request):
    form = Loginforms()    
    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForms()
    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
    pass