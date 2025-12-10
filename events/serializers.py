from rest_framework import serializers
from .models import EventTicket, Event
from companies.serializers import EnterpriseProfileCompleteSerializer


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTicket
        fields = [
            "id",
            "nome",
            "modalidade",
            "valor_receber",
            "valor_comprador",
            "quantidade_max_venda",
            "data_inicio",
            "data_fim"
        ]


class EventSerializer(serializers.ModelSerializer):
    # fk_empresa_id_empresa = EnterpriseProfileCompleteSerializer()
    # ticket = TicketSerializer()

    class Meta:
        model = Event
        fields = [
            "id",
            "nome",
            "data_inicio",
            "data_fim",
            "descricao",
            "imagem",
            "cep",
            "uf",
            "cidade",
            "bairro",
            "logradouro",
            "complemento",
            "numero",
            "destaque",
            "slug",
            "fk_empresa_id_empresa",
            "ticket"
        ]

class EventTicketSerializers(serializers.ModelSerializer):
    fk_id_evento = EventSerializer()

    class Meta:
        model = EventTicket
        fields = [
            "id",
            "nome",
            "modalidade",
            "data_inicio",
            "data_fim",
            "fk_id_evento"
        ]
