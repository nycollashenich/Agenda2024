from django.urls import path
from agenda.views import index, listadecontatos, no_contato, addcontato, excluir_contato, editar_contato

urlpatterns = [
    path('', index, name='index'),
    path('listadecontatos/', listadecontatos, name='listadecontatos'),
    path('contato/<int:pk>', no_contato, name='nocontato'),
    path('adicionarcontato/', addcontato, name='addcontato'),
    path('excluircontato/<int:id>/', excluir_contato, name='excluircontato'),
    path('editarcontato/<int:id>', editar_contato, name='editarcontato'),
]

