from django.db import models
from autoslug import AutoSlugField
import uuid

class EnterpriseProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cnpj = models.CharField(max_length=18, unique=True, null=True)
    logo = models.CharField(max_length=500, null=True)
    banner = models.CharField(max_length=500, null=True)
    sobre = models.TextField(null=True)
    slug = AutoSlugField(populate_from='get_slug_source')
    telefone = models.CharField(max_length=20)
    stripe_account_id = models.CharField(max_length=59, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    custom_user = models.OneToOneField(
        "authentication.CustomUser",
        on_delete=models.CASCADE,
        related_name='enterprise_profile'
    )

    def __str__(self):
        return self.slug
    
    def get_slug_source(self):
        return self.custom_user.first_name
    



#   evento            evento[]
#   venda             venda[]
#   avaliacao         avaliacao_evento[]
#   notificacao       notificacao[]
# }