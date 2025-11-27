from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .services import ProductServiceTable
from django.shortcuts import get_object_or_404
from .models import SaleProduct

import time

class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=True)

        if serializer.is_valid():
            products_instance = serializer.save()
            for product in products_instance:
               product_id = ProductServiceTable().AssembleForTable(product)
               time.sleep(4)
               client_id = product.client
               queue_product = ProductServiceTable().GetQueueProduct(product_id, client_id)
               print("===============RETURNED================")
               print(queue_product)
               sale = SaleProduct.objects.create(**queue_product)
               print("=========================SALE=====================")
               print(sale.__dict__)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

# class QueueOrder(APIView):
#     def post(self, request, pk):
#         sale = get_object_or_404(SaleProduct, )