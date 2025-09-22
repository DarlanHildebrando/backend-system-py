from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import jwt

class JWTAndCookieServices():
    @staticmethod
    def generate_token_and_set(user, flag=None):
        token = RefreshToken.for_user(user)
    
        if flag == 'Register':
            response = Response({"message": "Cadastrado e autenticado!"}, status=status.HTTP_201_CREATED)
        else:
            response = Response({"message": "Autenticado!"}, status=status.HTTP_200_OK)    

        response.set_cookie(
            key="access_token",
            value=str(token.access_token),
            httponly=True,
            secure=True,
            samesite="Strict"
        )

        response.set_cookie(
            key="refresh_token",
            value=str(token),
            httponly=True,
            secure=True,
            samesite="Strict"
        )
        return response
    
    @staticmethod
    def JWT_decode(token):
        try:
            paylod = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return Response({"message": "Token expirado!"})
        except jwt.InvalidTokenError:
            return Response({"message": "Token inválido!"})
        
        return paylod