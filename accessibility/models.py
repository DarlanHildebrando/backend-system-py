from django.db import models
import uuid

# Create your models here.

class Accessibility_Category(models.TextChoices):
    FISICA = 'FISICA', 'Fisica'
    AUDITIVA = 'AUDITIVA', 'Auditiva'
    VISUAL = 'VISUAL', 'Visual'
    COMUNICATIVA = 'COMUNICATIVA', 'Comunicativa'
    MOTORA = 'MOTORA', 'Motora'
    COGNITIVA = 'COGNITIVA', 'Cognitiva'

class Accessibility_Condition(models.TextChoices):
    EXCELENTE = 'EXCELENTE', 'Exelente'
    PRECARIA = 'PRECARIA', 'Precaria'
    RAZOAVEL = 'RAZOAVEL', 'Razoavel'
    NAO_UTILIZEI = 'NAO_UTILIZEI', 'Não utilizei'

class Accessibility_Type(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    categoria = models.CharField(max_length=30, choices=Accessibility_Category.choices)

    def __str__(self):
        return f"Acessibilidade: {self.nome}; id: {str(self.id)}" 

class Accessbility_Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_id_tipo_acessibilidade = models.ForeignKey(
        "accessibility.Accessibility_Type",
        on_delete=models.CASCADE,
        related_name='accessibility_registration'
    )
    fk_id_cliente = models.ForeignKey(
        "clients.ClientProfile",
        null=True,
        on_delete=models.CASCADE,
        related_name='client'
    )
    fk_id_evento = models.ForeignKey(
        "events.Event",
        null=True,
        on_delete=models.CASCADE,
        related_name='event'
    )

class Accessibility_Assessment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_id_tipo_acessibilidade = models.ForeignKey(
        "accessibility.Accessibility_Type",
        on_delete=models.CASCADE,
        related_name='accessibility_assessment'
    )
    estava_presente = models.BooleanField(default=False)
    condicao = models.CharField(max_length=30, choices=Accessibility_Condition.choices)
    avaliacao = models.ForeignKey(
        "events.Event_Evaluation",
        on_delete=models.CASCADE,
        related_name='accessibility_assessment'
    )

    def __str__(self):
        return self.condicao
