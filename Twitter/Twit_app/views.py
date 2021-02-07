from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User

from Twit_app.serializers import MessageSerializers, MessagePostSerializers
from Twit_app.models import Message


class Messages(APIView):
    """Сообщения чатов"""

    def get(self, request):
        comments = Message.objects.all()
        serializer = MessageSerializers(comments, many=True)
        return Response({"data":serializer.data})

    def post(self, request):
        # room = request.data.get("room")
        print(request.user)
        user=User.objects.get(id=request.user.id)
        
        dialog = Message(**request.data, user=user)
        dialog.save()
        return Response(status = 201)
            


class Dialogue(APIView):
    """Диалоги"""
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        room = request.GET.get("room")
        msg = Message.objects.filter(room=room)
        serializer = MessageSerializers(msg, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        # room = request.data.get("room")
        Message.objects.create()
        return Response(status=201)