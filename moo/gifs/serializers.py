from rest_framework import serializers
from .models import Gif


class GifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gif


class GifSearchSerializer(serializers.Serializer):
    query = serializers.CharField()
