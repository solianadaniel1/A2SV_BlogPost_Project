from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import CustomUser

user = get_user_model()


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = user
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):


    password = serializers.CharField(
        write_only=True
    )  # not to return the password after the user is created.

    class Meta:
        model = CustomUser
        fields = ["email", "username", "password"]

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            username=validated_data["username"],
        )
        return user
