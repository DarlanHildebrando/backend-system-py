from .serializers import RegisterCompletSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema


class CrudClient(APIView):
    @extend_schema(
        request=RegisterCompletSerializer,
        responses={201: RegisterCompletSerializer}
    )
    def post(self, request):
        serializer = RegisterCompletSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(f"message: 'Cadastrado!', data: {serializer.data}", status=status.HTTP_201_CREATED)
        else:
           return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)