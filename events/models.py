from django.db import models
import uuid

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