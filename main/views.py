from django.shortcuts import render
from rest_framework import generics
from .serializers import LampPostSerializer
from .models import LampPost
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


class LampPostCreateView(generics.CreateAPIView):
    serializer_class = LampPostSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):

        print('is_on' in request.POST)
        if 'is_on' in request.POST:
            if request.data['is_on'] == 'true':
                request.POST._mutable = True
                request.POST['on_time'] = datetime.now()
        else:
            request.POST._mutable = True
            request.POST['off_time'] = datetime.now()

        return self.create(request, *args, **kwargs)


class LampPostListView(generics.ListAPIView):
    serializer_class = LampPostSerializer
    queryset = LampPost.objects.all()
    permission_classes = (IsAuthenticated, )


class LampPostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LampPostSerializer
    queryset = LampPost.objects.all()
    permission_classes = (IsAuthenticated, )
    # TODO Сделать реализацию изменения параметров лампы
