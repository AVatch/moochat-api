import datetime

from rest_framework import serializers
from accounts.serializers import AccountSerializer

from threads.models import Thread
from gifs.models import Gif
from gifs.serializers import GifSerializer

from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    gif = GifSerializer(many=False, allow_null=True)
    
    class Meta:
        model = Note

    def create(self, validated_data):
      if validated_data['gif']:
          g, created = Gif.objects.get_or_create(**validated_data['gif'])
          n = Note.objects.create(author=validated_data['author'],
                                  gif=g, 
                                  content=validated_data['content'], 
                                  thread=validated_data['thread'])
      else:
          n = Note.objects.create(author=validated_data['author'],
                                  content=validated_data['content'], 
                                  thread=validated_data['thread'])

      t = Thread.objects.get(pk=validated_data['thread'])
      t.time_updated = datetime.datetime.now()
      t.save()
      
      return n
          