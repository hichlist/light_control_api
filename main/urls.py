from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('lamp_post/create/', LampPostCreateView.as_view()),
    path('lamp_post/all/', LampPostListView.as_view()),
    path('lamp_post/update/<int:pk>/', LampPostUpdateView.as_view())
]