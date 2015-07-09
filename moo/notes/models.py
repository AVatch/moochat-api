from django.db import models

from accounts.models import Account
from threads.models import Thread
from gifs.models import Gif


class Note(models.Model):
    author = models.ForeignKey(Account)
    thread = models.ForeignKey(Thread)
    content = models.TextField(blank=True)
    gif = models.ForeignKey(Gif, null=True)

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('time_created', )
