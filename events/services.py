from accessibility.models import Accessibility_Type, Accessbility_Registration
from accessibility.serializers import AccessibilityTypeSerializer

class EventUtils:

    @staticmethod
    def GetAccessibilitys(id):
        # Filtra todos os registros de acessibilidade do evento
        access_registration = Accessbility_Registration.objects.filter(fk_id_evento=id)

        # Extrai todos os IDs únicos de tipos de acessibilidade
        access_type_ids = access_registration.values_list("fk_id_tipo_acessibilidade", flat=True).distinct()

        # Busca os tipos correspondentes
        access_types = Accessibility_Type.objects.filter(id__in=access_type_ids)

        serializer = AccessibilityTypeSerializer(access_types, many=True)

        return serializer.data
    
    @staticmethod
    def AssembleObject(self, ):

        pass