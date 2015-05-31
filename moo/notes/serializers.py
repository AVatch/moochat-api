from rest_framework import serializers
from accounts.serializers import AccountSerializer

from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    author = AccountSerializer()
    class Meta:
        model = Note
          