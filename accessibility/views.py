from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from clients.models import VisualConfiguration, ClientProfile
from .serializers import AccessibilityConfigSerializer
from rest_framework.response import Response
from rest_framework import status

class VisualConfigurationView(APIView):
    def post(self, request):
        user = get_object_or_404(ClientProfile, id=request.data.get("fk_id_cliente"))
        serializer = AccessibilityConfigSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(fk_id_cliente_id=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)