from rest_framework import serializers


class GifSearchSerializer(serializers.Serializer):
    query = serializers.CharField()
