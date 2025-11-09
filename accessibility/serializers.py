from .models import Accessbility_Registration, Accessibility_Type
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from clients.models import VisualConfiguration

class AccessibilityConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualConfiguration
        fields = '__all__'

class AccessibilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessibility_Type
        fields = ["id", "nome", "descricao", "categoria"]

class AccessibilityRegistrationSerializer(serializers.ModelSerializer):
    fk_id_tipo_acessibilidade = Accessibility_Type()
    class Meta:
        model = Accessbility_Registration
        fields = [
            "id",
            "fk_id_cliente",
            "fk_id_evento",
            "fk_id_tipo_acessibilidade"
        ]

class Acc(serializers.ModelSerializer):
    fk_id_tipo_acessibilidade = AccessibilityTypeSerializer(read_only=True)
    class Meta:
        model = Accessbility_Registration
        fields = ["id", "fk_id_tipo_acessibilidade", "fk_id_cliente", "fk_id_evento"]