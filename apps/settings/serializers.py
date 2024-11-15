from rest_framework import serializers
from apps.users.models import User
from .models import Profile, PaymentInfo


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="user.id")
    email = serializers.EmailField(source="user.email")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")

    class Meta:
        model = Profile
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "bio",
            "position",
            "image",
        ]

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


class PaymentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentInfo
        fields = ["account_number", "bank_name", "billing_period", "state", "country"]
