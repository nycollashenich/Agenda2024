from django.db import models

# criando models que ficaram no banco de dados
# unique=True, usado para garantir que não terá dois valores iguais

class Contato(models.Model):
    primeiro_nome = models.CharField('Primeiro nome', max_length=100)
    segundo_nome = models.CharField('Segundo nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=15)
    email = models.EmailField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.primeiro_nome
