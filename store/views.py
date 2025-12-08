from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .services import ProductServiceTable
from django.shortcuts import get_object_or_404
from .models import SaleProduct, NotificationStore

import time
import uuid

class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=True)

        if serializer.is_valid():
            products_instance = serializer.save()
            for product in products_instance:
               client_id = product.client
               product_id = ProductServiceTable().AssembleForTable(product)
            #    time.sleep(4)
               
            #    queue_product = ProductServiceTable().GetQueueProduct(product_id, client_id)
            #    print("===============RETURNED================")
            #    print(queue_product)
               sale = SaleProduct.objects.create(**product_id)
               print("========================SALEEEE=====================")
               print(sale.__dict__)
            #    print("=========================SALE=====================")
            #    print(sale.__dict__)
               notification = NotificationStore.objects.create(sale=sale)
               print("====================NOTIFICATION================")
               print(notification.__dict__)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request):
    #     serializer

# class QueueOrder(APIView):
#     def post(self, request, pk):
#         sale = get_object_or_404(SaleProduct, )