from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class Client(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    imagem = models.CharField(max_length=15, blank=True, null=True)
    banner = models.CharField(max_length=500, blank=True, null=True)
    biografia = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=319, unique=True)
    inklua_coins = models.IntegerField(default=0)
    aceitaTermos = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.nome

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
        Client,
        on_delete=models.CASCADE,
        related_name="disability_type"
    )

    def __str__(self):
        return self.fisica

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_id_cliente = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name='notification'
    )
    fk_id_empresa = models.ForeignKey(
        "companies.Enterprise",
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


# model notificacao {
#   id_notificacao Int @id @default(autoincrement())
#   fk_id_cliente  Int
#   fk_id_empresa  Int
#   fk_id_evento   Int

#   lida         Boolean  @default(false)
#   data_criacao DateTime @default(now())
#   data_evento  DateTime
#   local_evento String   @db.VarChar(100)
#   nome_evento  String   @db.VarChar(100)
#   nome_empresa String   @db.VarChar(100)

#   cliente cliente @relation(fields: [fk_id_cliente], references: [id_cliente], onDelete: Cascade, onUpdate: Cascade)
#   empresa empresa @relation(fields: [fk_id_empresa], references: [id_empresa])
#   evento  evento  @relation(fields: [fk_id_evento], references: [id_evento])
# }
