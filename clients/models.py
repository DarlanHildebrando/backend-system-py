from django.db import models
import uuid

class ClientProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    imagem = models.CharField(max_length=15, blank=True, null=True)
    banner = models.CharField(max_length=500, blank=True, null=True)
    biografia = models.CharField(max_length=500, blank=True, null=True)
    inklua_coins = models.IntegerField(default=0)
    custom_user = models.OneToOneField(
        "authentication.CustomUser",
        on_delete=models.CASCADE,
        related_name="client_profile"
    )

    def __str__(self):
        return f"{self.custom_user.first_name}"

class ClientTicket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.UUIDField(default=uuid.uuid4)
    data_criacao = models.DateTimeField()
    salfk_id_vendae = models.ForeignKey(
        "events.SaleTickets",
        on_delete=models.CASCADE,
        related_name='client_ticket'
    )
    fk_id_ingresso = models.ForeignKey(
        "events.EventTicket",
        on_delete=models.CASCADE,
        related_name='client_ticket'
    )
    fk_id_cliente = models.ForeignKey(
        "clients.ClientProfile",
        on_delete=models.CASCADE,
        related_name='ticket'
    )



class Disability_Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fisica = models.BooleanField(default=False)
    auditiva = models.BooleanField(default=False)
    visual = models.BooleanField(default=False)
    comunicativa = models.BooleanField(default=False)
    cognitiva = models.BooleanField(default=False)
    outra = models.BooleanField(default=False)
    nao_possuo = models.BooleanField(default=False)
    nao_comentar = models.BooleanField(default=False)
    outra_texto = models.CharField(max_length=300, null=True, blank=True)
    cliente = models.OneToOneField(
        ClientProfile,
        on_delete=models.CASCADE,
        related_name="disability_type"
    )

    def __str__(self):
        return f"{self.id}"

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_id_cliente = models.ForeignKey(
        "clients.ClientProfile",
        on_delete=models.CASCADE,
        related_name='notification'
    )
    fk_id_empresa = models.ForeignKey(
        "companies.EnterpriseProfile",
        on_delete=models.CASCADE,
        related_name='notification'
    )
    fk_id_evento = models.ForeignKey(
        "events.Event",
        on_delete=models.CASCADE,
        related_name='notification'
    )
    lida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_evento = models.DateTimeField()
    nome_evento = models.CharField(max_length=100)
    local_evento = models.CharField(max_length=100)
    nome_empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.data_criacao

class VisualConfiguration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_alteracao =  models.CharField(max_length=255)
    value = models.IntegerField()
    nome_select = models.CharField(max_length=50)
    fk_id_cliente = models.ForeignKey(
        "clients.ClientProfile",
        on_delete=models.CASCADE,
        related_name='client'
    )
