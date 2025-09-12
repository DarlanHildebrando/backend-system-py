from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .services import generate_text

class GeminiAPI(APIView):
    def post(self, request):
        prompt = request.data.get("prompt", "")
        
        if not prompt:
            return Response({"error": 'Prompt obrigatório!'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            res = generate_text(prompt)
            return Response({"Texto gerado": res}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)