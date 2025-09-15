from .serializers import RegisterCompletSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.services import JWTAndCookieServices
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from authentication.models import CustomUser

class RegisterClientView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        request=RegisterCompletSerializer,
        responses={201: RegisterCompletSerializer}
    )
    def post(self, request):
        serializer = RegisterCompletSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           user = CustomUser.objects.get(id=serializer.data["custom_user"]["id"])
           response = JWTAndCookieServices.generate_token_and_set(user=user, flag='Register')
           return response
        else:
           return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class ClientProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        token = request.COOKIES.get("access_token")
        return Response(token, status=status.HTTP_200_OK)