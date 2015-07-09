from rest_framework import serializers
from accounts.serializers import AccountSerializer

from gifs.models import Gif
from gifs.serializers import GifSerializer

from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    gif = GifSerializer(many=False)
    
    class Meta:
        model = Note

    def create(self, validated_data):
      g, created = Gif.objects.get_or_create(**validated_data['gif'])
      n = Note.objects.create(author=validated_data['author'],
                              gif=g, 
                              content=validated_data['content'], 
                              thread=validated_data['thread'])
      return n
          