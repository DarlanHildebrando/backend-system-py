from rest_framework import serializers
from .models import EventTicket, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        # fields = [
        #     "id",
        #     "nome",
        #     "data_inicio",
        #     "data_fim",
        #     "descricao",
        #     "imagem",
        #     "cep",
        #     "uf",
        #     "cidade",
        #     "bairro",
        #     "logradouro",
        #     "complemento",
        #     "numero",
        #     "destaque",
        #     "slug",
        #     "fk_empresa_id_empresa"
        # ]

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