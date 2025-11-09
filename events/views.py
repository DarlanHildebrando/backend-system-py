from django.shortcuts import render
from rest_framework.views import APIView
from accessibility.models import Accessbility_Registration, Accessibility_Type
from accessibility.serializers import AccessibilityRegistrationSerializer, AccessibilityTypeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class AccessibilityEventsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        # Filtra todos os registros de acessibilidade do evento
        access_registration = Accessbility_Registration.objects.filter(fk_id_evento=pk)

        # Extrai todos os IDs únicos de tipos de acessibilidade
        access_type_ids = access_registration.values_list("fk_id_tipo_acessibilidade", flat=True).distinct()

        # Busca os tipos correspondentes
        access_types = Accessibility_Type.objects.filter(id__in=access_type_ids)

        serializer = AccessibilityTypeSerializer(access_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)