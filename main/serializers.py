from rest_framework import serializers
from .models import LampPost


class LampPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LampPost
        fields = '__all__'
