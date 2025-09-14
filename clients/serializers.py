from rest_framework import serializers
from .models import ClientProfile, Disability_Type
from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer
from django.contrib.auth.hashers import make_password
from accessibility.models import Accessibility_Type, Accessbility_Registration
from django.db import transaction

class AccessibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessbility_Registration
        fields = ["fk_id_tipo_acessibilidade"]

class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'
        extra_kwargs = {
            "custom_user": {"required": False, "allow_null": True}
        }

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

class RegisterCompletSerializer(serializers.Serializer):
    custom_user = CustomUserSerializer()
    client_profile = ClientProfileSerializer()
    disability = DisabilitySerializer()
    accessibilities = serializers.PrimaryKeyRelatedField(
        queryset=Accessibility_Type.objects.all(),
        many=True
    )

    @transaction.atomic
    def create(self, validated_data):

        user = validated_data.pop("custom_user")
        password = user.pop("password")
        user["password"] = make_password(password)

        user_created = CustomUser.objects.create(**user)

        client_data = validated_data.pop("client_profile")
        client_data["custom_user"] = user_created
        client = ClientProfileSerializer().create(client_data)

        disability_data = validated_data.pop("disability")
        disability = Disability_Type.objects.create(cliente=client, **disability_data)

        accessibilities = []
        accessibility_data = validated_data.pop("accessibilities")
        for accessibility in accessibility_data:
            accessibility_created = Accessbility_Registration.objects.create(fk_id_tipo_acessibilidade=accessibility, fk_id_cliente=client)
            accessibilities.append(accessibility_created)

        return {
            "custom_user": user_created,
            "client_profile": client,
            "disability": disability,
            "accessibilities": accessibilities,
          }