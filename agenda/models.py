from django.db import models
from stdimage.models import StdImageField

# criando models que ficaram no banco de dados
# unique=True, usado para garantir que não terá dois valores iguais

class Contato(models.Model):
    primeiro_nome = models.CharField('Primeiro nome', max_length=100, blank=False)
    segundo_nome = models.CharField('Segundo nome', max_length=100, blank=True)
    telefone = models.CharField('Telefone', max_length=15, blank=False)
    email = models.EmailField(unique=True, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    imagem = StdImageField('Imagem', upload_to='rostos_contatos', variations={'thumb': (124, 124)}, blank=True)

    def __str__(self) -> str:
        return self.primeiro_nome
