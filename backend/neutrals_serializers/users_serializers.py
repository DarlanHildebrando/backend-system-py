from accessibility.models import Accessbility_Registration
from rest_framework import serializers
from clients.models import ClientProfile, Disability_Type
from authentication.models import CustomUser
from accessibility.models import Accessbility_Registration


class AccessibilityRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessbility_Registration
        fields = '__all__'

class DisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disability_Type
        fields = [
            "id",
            "fisica",
            "auditiva",
            "visual",
            "comunicativa",
            "cognitiva",
            "outra",
            "nao_possuo",
            "nao_comentar",
            "outra_texto",
        ]

        read_only_fields = ["id"]

class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'
        extra_kwargs = {
            "custom_user": {"required": False, "allow_null": True}
        }


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            "password": {"write_only": True}
            }
