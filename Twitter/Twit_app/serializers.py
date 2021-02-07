from rest_framework import serializers
from django.contrib.auth.models import User

from Twit_app.models import Message



class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class MessageSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSerializer()
    class Meta:
        model = Message
        fields = ("user", "text", "date")


class MessagePostSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSerializer()
    class Meta:
        model = Message
        fields = ("user", "text")


