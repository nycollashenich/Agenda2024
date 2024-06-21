from django.urls import path
from agenda.views import index, listadecontatos

urlpatterns = [
    path('', index, name='index'),
    path('listadecontatos/', listadecontatos, name='listadecontatos'),
]