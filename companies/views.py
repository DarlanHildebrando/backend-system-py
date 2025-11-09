from rest_framework.views import APIView
from .serializers import EntRegisterCompletSerializer,EnterpriseProfileCompleteSerializer
from .models import EnterpriseProfile
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

class EnterpriseProfileView(APIView):

    def post(self, request, pk):
        user = EnterpriseProfile.objects.get(id=pk).custom_user
        print("=========user===========")
        print(user)
        serializer = EnterpriseProfileCompleteSerializer(user)
        print("=========SERIALIZER DATA===========")
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)