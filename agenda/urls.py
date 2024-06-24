from django.urls import path
from agenda.views import index, listadecontatos, editar_excluir, addcontato

urlpatterns = [
    path('', index, name='index'),
    path('listadecontatos/', listadecontatos, name='listadecontatos'),
    path('contato/<int:pk>', editar_excluir, name='editar_excluir'),
    path('adicionarcontato/', addcontato, name='addcontato')
]