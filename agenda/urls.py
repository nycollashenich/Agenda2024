from django.urls import path
from agenda.views import index, listadecontatos, editar_excluir

urlpatterns = [
    path('', index, name='index'),
    path('listadecontatos/', listadecontatos, name='listadecontatos'),
    path('contato/<int:pk>', editar_excluir, name='editar_excluir'),
]