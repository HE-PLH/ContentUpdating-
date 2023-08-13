from rest_framework import serializers
from django.contrib.auth.models import User


class TokenSerializer(serializers.Serializer):
    """
        This serializer serializes the token data
    """
    access_token = serializers.CharField(max_length=255)
    refresh_token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

