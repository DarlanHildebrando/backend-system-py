from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .backends import EmailBackend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        print("=====================================")
        print(email)
        password = request.data.get("password")
        print("=====================================")
        print(password)

        user = EmailBackend.authenticate(email=email, password=password)

        print(user)

        if user is not None:
           token = RefreshToken.for_user(user)

           response = Response({"details": "Login realizado com sucesso!"}, status=status.HTTP_200_OK)

           response.set_cookie(
               key="access_token",
               value=str(token.access_token),
               httponly=True,
               secure=True,
               samesite="Strict"
           )

           return response

        return Response({"detail": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)   

class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Logout realizado com sucesso!"}, status=status.HTTP_200_OK)
        response.delete_cookie("access_token")
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