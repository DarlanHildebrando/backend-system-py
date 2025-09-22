from rest_framework.views import APIView
from .serializers import EntRegisterCompletSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from authentication.models import CustomUser
from authentication.services import JWTAndCookieServices
from rest_framework.response import Response
from rest_framework import status

class CrudEnterprise(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        request=EntRegisterCompletSerializer,
        responses={201: EntRegisterCompletSerializer}
    )
    def post(self, request):
        serializer = EntRegisterCompletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = CustomUser.objects.get(id=serializer.data["custom_user"]["id"])
            response = JWTAndCookieServices.generate_token_and_set(user=user, flag='Register')
            return response
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)