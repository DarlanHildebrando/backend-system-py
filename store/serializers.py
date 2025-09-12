from rest_framework import serializers
from .models import Product
from clients.models import Client

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = [
            "id",
            "name",
            "color",
            "size",
            "icon",
            "client"
        ]

    def create(self, validated_data):
        client = validated_data.pop("client")
        client_data = Client.objects.get(id=client.id)
        product_created = Product.objects.create(client=client_data, **validated_data)

        return product_created