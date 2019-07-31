from django.shortcuts import render
from rest_framework import generics
from .serializers import LampPostSerializer


class LampPostCreateView(generics.CreateAPIView):
    serializer_class = LampPostSerializer

