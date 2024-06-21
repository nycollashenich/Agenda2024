from django.shortcuts import render
from .models import Contato

def index(request):
    return render(request, 'index.html')

def listadecontatos(request):
    contatos = Contato.objects.all()
    context = {
        'contatos': contatos,
    }

    return render(request, 'lista_de_contatos.html', context)