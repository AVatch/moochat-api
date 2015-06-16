from django.db import models
from accounts.models import Account
from threads.models import Thread


class Note(models.Model):
    author = models.ForeignKey(Account)
    thread = models.ForeignKey(Thread)
    content = models.TextField()
    
    is_gif = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('time_created', )
    