from rest_framework import serializers
from accounts.serializers import AccountSerializer

from .models import Thread

class ThreadSerializer(serializers.ModelSerializer):
    participants = AccountSerializer(many=True)
    class Meta:
        model = Thread

class ThreadStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
          