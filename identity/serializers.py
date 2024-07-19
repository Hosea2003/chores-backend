from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from identity.models import AppUser


class AppLoginSerializer(LoginSerializer):
    email = None


class AppUserDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    profile_picture = serializers.ImageField()

    class Meta:
        model = AppUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "profile_picture",
        ]
