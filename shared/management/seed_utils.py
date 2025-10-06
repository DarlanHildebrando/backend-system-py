from events.models import Event, EventTicket, EventAndCategory, EventAndHashtag, Hashtag, Category
from accessibility.models import Accessbility_Registration, Accessibility_Type
from datetime import datetime, timedelta
from random import sample
from django.core.management.color import color_style
import random

style = color_style()

class SeedUtils:
    def bulk_event(self, events, entprofile_instance):
        print(style.MIGRATE_HEADING("Criando eventos e ingressos..."))
        event_created = Event.objects.bulk_create(
                    [Event(nome=event["nome"],
                           data_inicio=event["data_inicio"],
                           data_fim=event["data_fim"],
                           descricao=event["descricao"],
                           imagem=event["imagem"],
                           capacidade=event["capacidade"],
                           cep=event["cep"],
                           uf=event["uf"],
                           cidade=event["cidade"],
                           bairro=event["bairro"],
                           logradouro=event["logradouro"],
                           complemento=event["complemento"],
                           numero=event["numero"],
                           destaque=event["destaque"],
                           fk_empresa_id_empresa=entprofile_instance)
                           for event in events
                           ])
        print(style.HTTP_INFO(f"Evento criado: {event_created}"))

        start_date = datetime.now() + timedelta(days=random.randint(0, 30))
        end_date = start_date + timedelta(hours=random.randint(1, 6))

        for event in event_created:

            tickets_to_create = [
                {
                    "nome": "PISTA TESTE 1",
                    "modalidade": "INTEIRA",
                    "valor_receber": 100.00,
                    "valor_comprador": '10',
                    "quantidade_max_venda": 5,
                    "data_inicio": start_date,
                    "data_fim": end_date,
                    "fk_id_evento": event,
                    "price_id": "price_1RY4rAPN721PjGWf17SSc0DX"
                },{
                    "nome": "PISTA TESTE 2",
                    "modalidade": "MEIA",
                    "valor_receber": 100.00,
                    "valor_comprador": '10',
                    "quantidade_max_venda": 5,
                    "data_inicio": start_date,
                    "data_fim": end_date,
                    "fk_id_evento": event,
                    "price_id": "price_1RY4rAPN721PjGWfqMPBUdEM"
                }
            ]

            for ticket in tickets_to_create:
                created = EventTicket.objects.create(**ticket)
                if created:
                    print(style.HTTP_INFO(f"Ingresso {created.nome} do evento {event.nome} criado!"))
                else:
                    print(style.ERROR("Não foi possível criar os ingressos."))

            self.event_relations(event)


    def event_relations(self, event):
        print(style.MIGRATE_HEADING("Criando relação entre hashtags e eventos..."))
        ids_hashtags = list(Hashtag.objects.values_list('id', flat=True))
        random_hashtags = Hashtag.objects.filter(id__in=sample(ids_hashtags, 5))
        eventAndHashtag = EventAndHashtag.objects.bulk_create([EventAndHashtag(
            fk_id_hashtag=hashtag,
            fk_id_evento=event,)
            for hashtag in random_hashtags
        ])
        print(style.HTTP_INFO(f"{eventAndHashtag}!"))

        print(style.MIGRATE_HEADING("Criando relação entre categorias e eventos..."))
        ids_categories = list(Category.objects.values_list('id', flat=True))
        random_category = Category.objects.get(id__in=sample(ids_categories, 1))
        eventAndCategory = EventAndCategory.objects.create(
            fk_id_categoria=random_category,
            fk_id_evento=event
        )
        print(style.HTTP_INFO(f"{eventAndCategory}!"))

        print(style.MIGRATE_HEADING("Criando relação entre accessibilidades e eventos..."))
        ids_accessibilities = list(Accessibility_Type.objects.values_list('id', flat=True))
        random_accessibilities = Accessibility_Type.objects.filter(id__in=sample(ids_accessibilities, 10))

        access_registration = Accessbility_Registration.objects.bulk_create(
            [Accessbility_Registration(
                fk_id_tipo_acessibilidade=accessibility,
                fk_id_evento=event
            )for accessibility in random_accessibilities]
        )
        for registration in access_registration:
            print(style.HTTP_INFO(f"{registration}"))