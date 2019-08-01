from django.shortcuts import render
from rest_framework import generics
from .serializers import LampPostSerializer
from .models import LampPost


class LampPostCreateView(generics.CreateAPIView):
    serializer_class = LampPostSerializer


class LampPostListView(generics.ListAPIView):
    serializer_class = LampPostSerializer
    queryset = LampPost.objects.all()


class LampPostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LampPostSerializer
    queryset = LampPost.objects.all()
