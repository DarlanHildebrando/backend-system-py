from django.db import models
import uuid

class Enterprise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    logo = models.CharField(max_length=500)
    banner = models.CharField(max_length=500)
    sobre = models.TextField()
    slug = models.CharField(max_length=255)
    email = models.EmailField(max_length=319, unique=True)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)
    stripe_account_id = models.CharField(max_length=59)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    



#   evento            evento[]
#   venda             venda[]
#   avaliacao         avaliacao_evento[]
#   notificacao       notificacao[]
# }