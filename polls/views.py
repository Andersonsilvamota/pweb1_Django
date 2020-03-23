from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, bem vindo ao meu site.")

def contatos(request):
    return HttpResponse('Essa é a view de CONTATOS do site. ')

def sobre(request):
    return HttpResponse('Essa é uma página SOBRE do site.')