from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .backends import CustomBackend
from rest_framework_simplejwt.views import TokenRefreshView
from .services import JWTAndCookieServices
from rest_framework.permissions import AllowAny, IsAuthenticated


class LoginView(APIView):
    def post(self, request):
        login_id = request.data.get("email")
        password = request.data.get("password")

        user = CustomBackend.authenticate(email=login_id, password=password)

        if user is not None:
           response = JWTAndCookieServices.generate_token_and_set(user)

           return response

        return Response({"detail": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)   

class LogoutView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        response = Response({"message": "Logout realizado com sucesso!"}, status=status.HTTP_200_OK)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response

class CookieJWTRefresh(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")
        if refresh_token is None:
            return Response({'Error': 'Refresh Token não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
        data = {"refresh": refresh_token}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        access_token = serializer.validated_data["access"]

        response = Response({"detail": "Token atualizado!"}, status=status.HTTP_200_OK)
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Strict"
        )

        return response

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user:
            if user.user_type == 'CLIENT':
                return Response(
                    {
                        "user_id": user.id,
                        "user_email": user.email,
                        "user_profile": user.client_profile.id
                    }, 
                    status=status.HTTP_200_OK
                )
            elif user.user_type == 'ENTERPRISE':
                return Response(
                    {
                        "user_id": user.id,
                        "user_email": user.email,
                        "user_profile": user.enterprise_profile.id,
                        "cnpj": user.enterprise_profile.cnpj
                    }, 
                    status=status.HTTP_200_OK
                ) 
        else:
            return Response(
                {"message": "Usuário não logado!"},
                status=status.HTTP_200_OK
            )