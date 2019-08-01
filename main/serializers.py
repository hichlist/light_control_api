from rest_framework import serializers
from .models import LampPost


class LampPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LampPost
        fields = ('lamp_id', 'brightness', 'is_on', 'on_time', 'off_time')
