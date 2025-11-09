from rest_framework import serializers
from .models import EnterpriseProfile
from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer
from django.contrib.auth.hashers import make_password
from django.db import transaction

class EnterpriseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseProfile
        fields = '__all__'
        extra_kwargs = {
            "custom_user": {"required": False, "allow_null": True}
        }

class EnterpriseProfileCompleteSerializer(serializers.ModelSerializer):
    enterprise_profile = EnterpriseProfileSerializer()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "first_name",
            "enterprise_profile"
        ]

class EntRegisterCompletSerializer(serializers.Serializer):
    custom_user = CustomUserSerializer()
    enterprise_profile = EnterpriseProfileSerializer()

    @transaction.atomic
    def create(self, validated_data):
        user = validated_data.pop("custom_user")
        password = user.pop("password")
        user["password"] = make_password(password)
        user_created = CustomUser.objects.create(**user)

        enterprise = validated_data.pop("enterprise_profile")
        enterprise["custom_user"] = user_created
        enterprise_created = EnterpriseProfile.objects.create(**enterprise)

        return {
            "custom_user": user_created,
            "enterprise_profile": enterprise_created
        }


