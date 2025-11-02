from rest_framework import serializers
from .models import Disability_Type, ClientProfile
from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer
from .services import Profile
from django.contrib.auth.hashers import make_password
from accessibility.models import Accessibility_Type, Accessbility_Registration
from django.db import transaction
import uuid

import logging
logger = logging.getLogger("clients")

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


class RegisterCompletSerializer(serializers.Serializer):
    custom_user = CustomUserSerializer()
    client_profile = ClientProfileSerializer()
    disability_type = DisabilitySerializer()
    access_registration = serializers.PrimaryKeyRelatedField(
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

        disability_data = validated_data.pop("disability_type")
        disability = Disability_Type.objects.create(cliente=client, **disability_data)

        accessibilities = []
        accessibility_data = validated_data.pop("access_registration")
        for accessibility in accessibility_data:
            accessibility_created = Accessbility_Registration.objects.create(fk_id_tipo_acessibilidade=accessibility, fk_id_cliente=client)
            accessibilities.append(accessibility_created)

        return {
            "custom_user": user_created,
            "client_profile": client,
            "disability_type": disability,
            "access_registration": accessibilities,
          }

class GetClientProfileSerializer(serializers.ModelSerializer):
    disability_type = DisabilitySerializer()
    
    class Meta:
        model = ClientProfile
        fields = ["id", 
                  "telefone",
                  "imagem",
                  "banner",
                  "biografia",
                  "inklua_coins",
                  "notification",
                  "disability_type",]
        extra_kwargs = {
            "custom_user": {"required": False, "allow_null": True}
        }

class GetProfileSerializer(serializers.ModelSerializer):
    client_profile = GetClientProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ["id", 
                  "username",
                  "first_name",
                  "email",
                  "user_type",
                  "client_profile",
                ]


class PatchProfileSerializer(serializers.ModelSerializer):
    disability_type = DisabilitySerializer()

    class Meta:
        model = ClientProfile
        fields = ["id", 
                  "telefone",
                  "imagem",
                  "banner",
                  "biografia",
                  "inklua_coins",
                  "aceitaTermos",
                  "disability_type",
                  ]
        extra_kwargs = {
            "custom_user": {"required": False, "allow_null": True}
        }

class PatchUserSerializer(serializers.ModelSerializer):
    client_profile = PatchProfileSerializer()
    class Meta:
        model = CustomUser
        fields = ["id", 
                  "username",
                  "email",
                  "user_type",
                  "client_profile"
                ]
        
    def update(self, instance, validated_data):
        print("==================================================================")
        profile = Profile.updateProfile(validated_data)

        return instance