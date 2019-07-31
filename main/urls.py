from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('lamp_post/create/', LampPostCreateView.as_view())
]