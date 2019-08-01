from django.shortcuts import render
from rest_framework import generics
from .serializers import LampPostSerializer
from .models import LampPost
from rest_framework.permissions import IsAuthenticated


class LampPostCreateView(generics.CreateAPIView):
    serializer_class = LampPostSerializer
    permission_classes = (IsAuthenticated, )


class LampPostListView(generics.ListAPIView):
    serializer_class = LampPostSerializer
    queryset = LampPost.objects.all()
    permission_classes = (IsAuthenticated, )


class LampPostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LampPostSerializer
    queryset = LampPost.objects.all()
    permission_classes = (IsAuthenticated, )
