from django.shortcuts import render, redirect

def login(request):
    return render(request, "login.html")

def Listagem_de_tarefas(request):
    return render(request, "Listagem_de_tarefas.html")

def cadastro_de_tarefas(request):
    return render(request, "cadastro_de_tarefas.html")

def cadastro_de_usuarios(request):
    return render(request, "cadastro_de_usuários.html")
