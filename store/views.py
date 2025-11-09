from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .services import ProductServiceTable


class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=True)

        if serializer.is_valid():
            print("===================PRODUCT===================")
            print(serializer.data)
            products_instance = serializer.save()
            for product in products_instance:
                ProductServiceTable().AssembleForTable(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)