from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .services import ProductServiceTable
from django.shortcuts import get_object_or_404
from .models import SaleProduct

class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=True)

        if serializer.is_valid():
            products_instance = serializer.save()
            for product in products_instance:
                ProductServiceTable().AssembleForTable(product)
                # sale = SaleProduct.objects.create()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

# class QueueOrder(APIView):
#     def post(self, request, pk):
#         sale = get_object_or_404(SaleProduct, )