from django.db import models
import uuid

class Modalities(models.TextChoices):
    inteira = 'INTEIRA', 'Inteira'
    meia = 'MEIA', 'Meia'




class EventAndCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_id_categoria = models.ForeignKey(
        "events.Category",
        on_delete=models.CASCADE,
        related_name='event_and_category'
    )
    fk_id_evento = models.ForeignKey(
        "events.Event",
        on_delete=models.CASCADE,
        related_name='event_and_category'
    )

class EventAndHashtag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_id_hashtag = models.ForeignKey(
        "events.Hashtag",
        on_delete=models.CASCADE,
        related_name='event_and_hashtag'
    )
    fk_id_evento = models.ForeignKey(
        "events.Event",
        on_delete=models.CASCADE,
        related_name='event_and_hashtag'
    )

class Hashtag(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
    
class Category(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class SaleTickets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_criacao = models.DateTimeField()
    checkout_session_id = models.CharField(max_length=70)
    clienteId_cliente = models.ForeignKey(
        "clients.ClientProfile",
        on_delete=models.CASCADE,
        related_name='sales'
    )
    empresaId_empresa = models.ForeignKey(
        "companies.EnterpriseProfile",
        on_delete=models.CASCADE,
        related_name='sales'
    )


class EventTicket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=100, choices=Modalities.choices)
    valor_receber = models.DecimalField(max_digits=10, decimal_places=2)
    valor_receber = models.DecimalField(max_digits=10, decimal_places=2)
    valor_receber = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_max_venda = models.IntegerField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    fk_id_evento = models.ForeignKey(
        "events.Event",
        on_delete=models.CASCADE,
        related_name='ticket'
    )
    price_id = models.CharField(max_length=64)
    

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    descricao = models.CharField(max_length=300)
    imagem = models.CharField(max_length=500)
    capacidade = models.IntegerField()
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    destaque = models.BooleanField(default=False)
    slug = models.CharField(max_length=255)
    fk_empresa_id_empresa = models.ForeignKey(
        "companies.EnterpriseProfile",
        on_delete=models.CASCADE,
        related_name='events'
    )

    def __str__(self):
        return self.nome

class Event_Evaluation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_id_evento = models.ForeignKey(
        "events.Event",
        on_delete=models.CASCADE,
        related_name='event_evaluation'
    )
    fk_id_cliente = models.ForeignKey(
        "clients.ClientProfile",
        on_delete=models.CASCADE,
        related_name='event_evaluation'
    )
    fk_id_empresa = models.ForeignKey(
        "companies.EnterpriseProfile",
        on_delete=models.CASCADE,
        related_name='event_evaluation'
    )
    data = models.DateTimeField(auto_now_add=True)
    confianca_empresa = models.IntegerField(default=0)
    comentario_geral = models.CharField(max_length=300)

    def __str__(self):
        return self.data

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comentario = models.CharField(max_length=500)
    data_criacao = models.DateTimeField()
    fk_cliente_id_cliente = models.ForeignKey(
        "clients.ClientProfile",
        on_delete=models.CASCADE,
        related_name="comment"
    )
    fk_evento_id_evento = models.ForeignKey(
        "events.Event",
        on_delete=models.CASCADE,
        related_name='comment'
    )



# model avaliacao_evento {
#   id_avaliacao_evento      Int                        @id @default(autoincrement())
#   fk_id_evento             Int
#   fk_id_cliente            Int
#   fk_id_empresa            Int
#   data                     DateTime                   @default(now())
#   // Confiança geral na empresa (nota de 1 a 10)
#   confianca_empresa        Int
#   // Comentário geral sobre o evento
#   comentario_geral         String?
#   // Relações
#   avaliacao_acessibilidade avaliacao_acessibilidade[]
#   cliente                  cliente                    @relation(fields: [fk_id_cliente], references: [id_cliente], onDelete: Cascade, onUpdate: Cascade)
#   evento                   evento                     @relation(fields: [fk_id_evento], references: [id_evento], onDelete: Cascade, onUpdate: Cascade)
#   empresa                  empresa                    @relation(fields: [fk_id_empresa], references: [id_empresa], onDelete: Cascade, onUpdate: Cascade)
# }

#   fk_empresa_id_empresa   Int?
#   empresa                 empresa?                  @relation(fields: [fk_empresa_id_empresa], references: [id_empresa], onDelete: Cascade, onUpdate: NoAction)
#   comentario              comentario[]
#   ingresso                ingresso[]
#   contem_pertence         contem_pertence[]
#   pertence_associada      pertence_associada[]
#   acessibilidade_registro acessibilidade_registro[]
#   avaliacoes_evento       avaliacao_evento[]
#   notificacao             notificacao[]

#   @@index([fk_empresa_id_empresa], map: "idx_fk_empresa_evento")
# }