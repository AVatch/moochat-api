from django.db import models
from accounts.models import Account


class Thread(models.Model):
    participants = models.ManyToManyField(Account, related_name='threads')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('time_created', )
        
    def add_participant(self, account):
        pass
    
    def remove_participant(self, account):
        pass
