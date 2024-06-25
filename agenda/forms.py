from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['primeiro_nome', 'segundo_nome', 'telefone', 'email', 'descricao']