from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Contato


def index(request):
    return render(request, 'index.html')

def listadecontatos(request):
    contatos = Contato.objects.all()
    context = {
        'contatos': contatos,
    }

    return render(request, 'lista_de_contatos.html', context)

def editar_excluir(request, pk):
    cont = get_object_or_404(Contato, id=pk)
    context= {
        'contato': cont, # 'contato = for no template da lista'
    }
    return render(request, 'editar_excluir.html', context)





# def de erros, 404 e 500

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type= 'text/html; charset=utf8', status= 404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type= 'text/html; charset=utf8', status= 500)