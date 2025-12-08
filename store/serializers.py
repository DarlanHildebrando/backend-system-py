from rest_framework import serializers
from .models import Product, SaleProduct, NotificationStore
from clients.models import ClientProfile

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = [
            "id",
            "name",
            "color",
            "size",
            "icon",
            "client",
            "phrase",
            "typography"
        ]

    def create(self, validated_data):
        client = validated_data.pop("client")
        client_data = ClientProfile.objects.get(id=client.id)
        product_created = Product.objects.create(client=client_data, **validated_data)

        return product_created

class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleProduct
        fields = '__all__'



class NotificationStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStore
        fields = '__all__'

class SaleProfileSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    notification = NotificationStoreSerializer()
    class Meta:
        model = SaleProduct
        fields = [
            "id",
            "queue_order_id",
            "sale_date",
            "delivery_forecast",
            "status",
            "status_start_date",
            "status_finished_date",
            "preparation",
            "ready",
            "delivered",
            "product",
            "notification"
        ]
