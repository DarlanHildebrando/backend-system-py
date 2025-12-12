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
               queue_product = ProductServiceTable().GetQueueProduct(product_id, client_id)
               sale = SaleProduct.objects.create(**queue_product, product_id=product.id)
               NotificationStore.objects.create(sale=sale)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        sale = get_object_or_404(SaleProduct, id=pk)

        ProductServiceTable().GetQueueProduct(
            sale.queue_order_id, sale.client.id, True
            )
        
        atualized_sale = get_object_or_404(SaleProduct, id=pk)

        return Response(atualized_sale)



# class QueueOrder(APIView):
#     def post(self, request, pk):
#         sale = get_object_or_404(SaleProduct, id=pk)

#         queue_product = ProductServiceTable().GetQueueProduct(
#             sale.queue_order_id, sale.client.id, True
#             )
#         print("================QUEUE PRODUCT==============")
#         print(queue_product)

#         return queue_product
