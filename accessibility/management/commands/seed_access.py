from django.core.management import BaseCommand
from accessibility.models import Accessibility_Type

class Command(BaseCommand):
    help = 'Popula a tabela Accessibility_Type'

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.MIGRATE_HEADING("Criando Acessibilidades..."))

        accessibility_to_create = [
            # // FISICA
            { "nome": "Rampas de acesso", "descricao": "Estruturas inclinadas para substituir escadas e facilitar o acesso de cadeiras de rodas", "categoria": "FISICA" },
            { "nome": "Banheiros adaptados", "descricao": "Sanitários com barras de apoio, espaço para cadeira de rodas e portas largas", "categoria": "FISICA" },
            { "nome": "Elevadores acessíveis", "descricao": "Comandos em altura adequada, botões em braile e espaço interno para cadeiras de rodas", "categoria": "FISICA" },
            { "nome": "Mapas táteis com rotas acessíveis", "descricao": "Representações físicas do espaço com indicação de trajetos acessíveis", "categoria": "FISICA" },
            { "nome": "Corrimãos contínuos", "descricao": "Apoios firmes em rampas e escadas para auxílio na locomoção", "categoria": "FISICA" },
            { "nome": "Vagas reservadas para PCD", "descricao": "Estacionamentos próximos à entrada para pessoas com mobilidade reduzida", "categoria": "FISICA" },
            { "nome": "Cadeiras de rodas disponíveis no local", "descricao": "Empréstimo de cadeiras para quem necessita durante o evento", "categoria": "FISICA" },
            { "nome": "Mesas adaptadas", "descricao": "Altura e espaço livre sob a mesa para usuários de cadeira de rodas", "categoria": "FISICA" },
            { "nome": "Sinalização de piso antiderrapante", "descricao": "Pisos que evitam escorregões, facilitando o deslocamento seguro", "categoria": "FISICA" },
            { "nome": "Portas automáticas ou de fácil abertura", "descricao": "Facilitam o acesso sem exigir esforço físico", "categoria": "FISICA" },

            # // AUDITIVA
            { "nome": "Sistema de aviso visual", "descricao": "Alertas luminosos para emergências e anúncios", "categoria": "AUDITIVA" },
            { "nome": "Material em vídeo com Libras", "descricao": "Explicações gravadas com tradução em Libras", "categoria": "AUDITIVA" },
            { "nome": "Totem com atendimento por chat", "descricao": "Atendimento digital via texto para quem não escuta", "categoria": "AUDITIVA" },
            { "nome": "Intérpretes de Libras ao vivo", "descricao": "Profissionais traduzindo falas em tempo real", "categoria": "AUDITIVA" },
            { "nome": "Aplicativo com legendas em tempo real", "descricao": "Legendas automáticas sincronizadas com o áudio do evento", "categoria": "AUDITIVA" },
            { "nome": "Fones de vibração", "descricao": "Dispositivos que vibram conforme o som do ambiente", "categoria": "AUDITIVA" },
            { "nome": "Paineis de LED informativos", "descricao": "Mensagens escritas em telões para anúncios importantes", "categoria": "AUDITIVA" },
            { "nome": "Luzes sincronizadas com o palco", "descricao": "Luzes piscando em sincronia com som para percepção musical", "categoria": "AUDITIVA" },
            { "nome": "Comunicadores de emergência por texto", "descricao": "Permitem pedir ajuda via mensagem", "categoria": "AUDITIVA" },
            { "nome": "Folhetos informativos com Libras por QR Code", "descricao": "Materiais impressos com vídeos explicativos via QR", "categoria": "AUDITIVA" },

            # // VISUAL
            { "nome": "Sinalização em braille", "descricao": "Mapas, placas e sinalizações em braille", "categoria": "VISUAL" },
            { "nome": "Alto contraste nas sinalizações", "descricao": "Placas e avisos com contraste visual elevado", "categoria": "VISUAL" },
            { "nome": "Totens com leitores de tela compatíveis", "descricao": "Dispositivos digitais adaptados para leitura de tela", "categoria": "VISUAL" },
            { "nome": "Guias táteis do local", "descricao": "Mapas em relevo com o layout do espaço", "categoria": "VISUAL" },
            { "nome": "Aplicativo com navegação por voz", "descricao": "Descreve o caminho e eventos em áudio", "categoria": "VISUAL" },
            { "nome": "Cordões de orientação para cegos", "descricao": "Cordas-guia para orientação em filas e espaços amplos", "categoria": "VISUAL" },
            { "nome": "Funcionários-guia", "descricao": "Pessoas treinadas para acompanhar visitantes com deficiência visual", "categoria": "VISUAL" },
            { "nome": "Cartazes com fonte ampliada", "descricao": "Textos grandes para baixa visão", "categoria": "VISUAL" },
            { "nome": "Caminhos táteis no chão", "descricao": "Trilhas em relevo para guiar até pontos estratégicos", "categoria": "VISUAL" },
            { "nome": "Leitores portáteis disponíveis", "descricao": "Equipamentos que leem texto em voz alta", "categoria": "VISUAL" },

            # // COGNITIVA
            { "nome": "Suporte de acompanhante", "descricao": "Acompanhante pode entrar gratuitamente mediante laudo", "categoria": "COGNITIVA" },
            { "nome": "Orientação simplificada", "descricao": "Guias com linguagem direta e objetiva", "categoria": "COGNITIVA" },
            { "nome": "Evita estímulos sensoriais excessivos", "descricao": "Sem luzes piscantes ou sons estridentes", "categoria": "COGNITIVA" },
            { "nome": "Mapas ilustrados", "descricao": "Materiais com ícones e desenhos claros", "categoria": "COGNITIVA" },
            { "nome": "Espaços de descompressão", "descricao": "Áreas tranquilas para quem precisa se acalmar", "categoria": "COGNITIVA" },
            { "nome": "Agenda visual do evento", "descricao": "Calendário com ícones e cores para facilitar compreensão", "categoria": "COGNITIVA" },
            { "nome": "Fichas de instrução passo a passo", "descricao": "Cartões explicativos com imagens", "categoria": "COGNITIVA" },
            { "nome": "Equipe treinada em neurodiversidade", "descricao": "Funcionários capacitados para lidar com diferentes perfis cognitivos", "categoria": "COGNITIVA" },
            { "nome": "Pulseiras de identificação com preferências", "descricao": "Indicam se a pessoa aceita ou não contato visual, por exemplo", "categoria": "COGNITIVA" },
            { "nome": "Filas prioritárias com auxílio", "descricao": "Orientação reforçada nas filas para quem precisa", "categoria": "COGNITIVA" },

            # //FALA
            { "nome": "Equipe treinada em comunicação alternativa", "descricao": "Profissionais treinados para se comunicar por gestos, escrita ou recursos visuais.", "categoria": "COMUNICATIVA" },
            { "nome": "Tablets ou quadros brancos disponíveis", "descricao": "Ferramentas para escrita/digitalização disponíveis no evento para facilitar o diálogo.", "categoria": "COMUNICATIVA" },
            { "nome": "Pictogramas em áreas-chave", "descricao": "Sinalização visual com ícones simples que auxiliam na comunicação rápida e direta.", "categoria": "COMUNICATIVA" },
            { "nome": "Aplicativos de COMUNICATIVA digital", "descricao": "Apps que transformam texto digitado em voz", "categoria": "COMUNICATIVA" },
            { "nome": "Cards de comunicação rápida", "descricao": "Cartões com frases e símbolos comuns", "categoria": "COMUNICATIVA" },
            { "nome": "Totens interativos com texto predefinido", "descricao": "Opções clicáveis para expressar necessidades básicas", "categoria": "COMUNICATIVA" },
            { "nome": "Crachás com instruções de comunicação", "descricao": "Identificação com instruções como 'prefiro escrever'", "categoria": "COMUNICATIVA" },
            { "nome": "Intérpretes de comunicação alternativa", "descricao": "Profissionais especializados em comunicação não verbal", "categoria": "COMUNICATIVA" },
            { "nome": "Formulários visuais de feedback", "descricao": "Permitem apontar imagens ou emojis em vez de escrever", "categoria": "COMUNICATIVA" },
            { "nome": "Espaços com baixa interferência sonora", "descricao": "Ambientes mais calmos para facilitar a comunicação não verbal", "categoria": "COMUNICATIVA" },
        ]

        for accessibility in accessibility_to_create:
            accessibility_created = Accessibility_Type.objects.create(**accessibility)

            self.stdout.write(self.style.HTTP_INFO(f"\nAcessibilidade criada: {accessibility_created.nome} ; Categoria: {accessibility_created.categoria} ; Descrição: {accessibility_created.descricao}"))