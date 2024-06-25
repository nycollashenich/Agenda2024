from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Contato
from agenda.forms import ContatoForm
from django.contrib import messages


# index, página inicial
def index(request):
    return render(request, 'index.html')


# lista de contatos, mostra todos meus contatos com Contato.objects.all()
def listadecontatos(request):
    contatos = Contato.objects.all()
    context = {
        'contatos': contatos
    }
    return render(request, 'lista_de_contatos.html', context)


# edição e exclusão dos contatos
def no_contato(request, pk):
    cont = get_object_or_404(Contato, id=pk)
    context = {
        'contato': cont,
    }
    return render(request, 'no_contato.html', context)


# adiconar um novo contato;
def addcontato(request):
    form = ContatoForm()
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, 'O contato foi salvo.')
            return HttpResponseRedirect(reverse('listadecontatos')) 
    return render(request, 'addcontato.html', {'form' : form})

def excluir_contato(request, id):
    contato = Contato.objects.get(id=id)
    contato.delete()
    messages.success(request, 'O post foi excluido.')
    return HttpResponseRedirect(reverse('listadecontatos'))

def editar_contato(request, id):
    cont = get_object_or_404(Contato, id=id) # id do post
    form = ContatoForm(request.POST or None, request.FILES or None, instance=cont)
    if form.is_valid(): # se for valido
        form.save() # salva
        messages.success(request, 'O contato foi atualizado com sucesso')
        return HttpResponseRedirect(reverse('listadecontato'))
    return render(request, 'editar_contato.html', {'cont': form})


# def de erros, 404 e 500
def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type= 'text/html; charset=utf8', status= 404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type= 'text/html; charset=utf8', status= 500)