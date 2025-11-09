from .serializers import RegisterCompletSerializer, GetProfileSerializer, PatchUserSerializer, ClientTicketsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.services import JWTAndCookieServices
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from authentication.models import CustomUser
from accessibility.models import Accessbility_Registration
from .services import Profile
from .models import ClientTicket
import logging

logger = logging.getLogger("clients")

class RegisterClientView(APIView):
    permission_classes = [AllowAny]
    # @extend_schema(
    #     request=RegisterCompletSerializer,
    #     responses={201: RegisterCompletSerializer}
    # )
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
        user = Profile.return_user(request)

        serializer = GetProfileSerializer(user)
        profile_data = serializer.data.copy()

        profile_complete = Profile.assemble_profile(profile_data, user)

        return Response(profile_complete, status=status.HTTP_200_OK)
    
    def patch(self, request):
        user = Profile.return_user(request)

        serializer = PatchUserSerializer(user, data=request.data, partial=True)
        # acc = Accessbility_Registration.objects.filter(id__in=request.data["access_registration"]["delete"]).delete()
        # logger.info("====================================================")
        # logger.info(acc)
        
        
        serializer.is_valid(raise_exception=True)

        return Response(user.id, status=status.HTTP_200_OK)

class ClientTicketsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        tickets = ClientTicket.objects.filter(fk_id_cliente=pk)
        serializer = ClientTicketsSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)