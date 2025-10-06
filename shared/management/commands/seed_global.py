from accessibility.models import Accessbility_Registration
from authentication.models import CustomUser
from clients.models import ClientProfile
from companies.models import EnterpriseProfile
from events.models import Event, Category, Hashtag
from django.core.management import call_command
from django.core.management.base import BaseCommand
from clients.serializers import RegisterCompletSerializer
from companies.serializers import EntRegisterCompletSerializer
from ...management.seed_utils import SeedUtils

import os
import random
import json

class Command(BaseCommand):
    help = 'seed global para popular o banco'

    def handle(self, *args, **options):
        call_command('seed_access')
        utils = SeedUtils()

        base_dir = os.path.dirname(__file__)
        clientP_path = os.path.join(base_dir, "..", "..", "json", "seedG_client.json")

        with open(clientP_path, "r", encoding='utf-8') as c:
            data = json.load(c)
        
        self.stdout.write(self.style.MIGRATE_HEADING("Criando usuários"))
        for person in data:
            serializer = RegisterCompletSerializer(data=person)
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.HTTP_INFO(f"Cliente criado: {serializer.data["custom_user"]}"))
            else:
                print(serializer.errors)
        
        categories = [
            "Esporte", 
            "Tecnologia", 
            "Shows", 
            "Gastronomia", 
            "Negócios"
        ]

        self.stdout.write(self.style.MIGRATE_HEADING('Criando categorias...'))
        categories_created = Category.objects.bulk_create([Category(nome=c) for c in categories])
        self.stdout.write(self.style.HTTP_INFO(f'Categorias criadas: {categories_created}'))

        hashtags = [
          "InteligenciaArtificial", "VidaLoka", "Felicidade", "Tecnologia", "Saúde",
          "Educação", "Viagens", "Arte", "Música", "Cultura", "Gastronomia",
          "Empreendedorismo", "Inovação", "Networking", "Eventos", "Diversão",
          "Experiências", "Aprendizado", "Criatividade", "Colaboração", "Comunidade",
          "Sustentabilidade", "TecnologiaVerde", "SaúdeMental", "BemEstar",
          "Autoconhecimento", "Motivação", "Empoderamento", "Diversidade", "Inclusão",
        ]

        self.stdout.write(self.style.MIGRATE_HEADING('Criando Hashtags...'))
        hashtags_created = Hashtag.objects.bulk_create([Hashtag(nome=h) for h in hashtags])
        self.stdout.write(self.style.HTTP_INFO(f'Hashtags criadas: {hashtags_created}'))

        companiesJ_path = os.path.join(base_dir, "..", "..", "json", "seedG_companies.json")
        eventsJ_path = os.path.join(base_dir, "..", "..", "json", "seedG_events.json")

        with open(eventsJ_path, "r", encoding='utf-8') as events:
            events_data = json.load(events)

        with open(companiesJ_path, "r", encoding='utf-8') as companies:
            companies_data = json.load(companies)
        
        count = 0

        self.stdout.write(self.style.MIGRATE_HEADING("Criando empresas..."))
        for enterprise in companies_data:
            serializer = EntRegisterCompletSerializer(data=enterprise)
            if serializer.is_valid():
                serializer.save()
                count += 1

                self.stdout.write(self.style.HTTP_INFO(f'Empresa criada: {serializer.data["custom_user"]["first_name"]}'))
                entprofile_instance = EnterpriseProfile.objects.get(id=serializer.data["enterprise_profile"]["id"])

                if len(events_data) <= 5:
                    num_events = len(events_data)
                else:    
                    num_events = random.randint(1, min(15, len(events_data)))

                events = random.sample(events_data, num_events)
                utils.bulk_event(events, entprofile_instance)

                events_data = [e for e in events_data if e not in events]

                if count == 6 and len(events_data) > 0: 
                    utils.bulk_event(events_data, entprofile_instance)

            else:
                self.stdout.write(self.style.ERROR(f'Erro ao criar empresa: {serializer.errors}'))
        self.stdout.write(self.style.SUCCESS("Seed Global completado com sucesso!"))
