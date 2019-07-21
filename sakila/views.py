from django.shortcuts import render
from rest_framework import viewsets, permissions
from sakila.serializers import ActorSerializer
from sakila.models import Actor

# Create your views here.
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ActorSerializer
