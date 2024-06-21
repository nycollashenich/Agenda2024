from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def listadecontatos(request):
    return render(request, 'lista_de_contatos.html')