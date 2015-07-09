from django.db import models


class Gif(models.Model):    
    url = models.URLField()
    webp = models.URLField(blank=True)
    mp4 = models.URLField(blank=True)

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
  
    class Meta:
        ordering = ('time_created', )