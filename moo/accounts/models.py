from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class AccountManager(BaseUserManager):
    def create_user(self, password=None, **kwargs):
        if not kwargs.get('username'):
            raise ValueError('User must have a valid username')

        account = self.model(
            username=kwargs.get('username'),
        )

        if password is None:
            raise ValueError('User must have a valid password')

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, password, **kwargs):
        account = self.create_user(password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    profile_picture_url = models.URLField(default="http://placehold.it/150x150")
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    phonenumber = models.CharField(max_length=15, blank=True)
    friends = models.ManyToManyField("self", blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    # Define custom manager
    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('time_created', )

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])
    
    def add_friend(self, account):
        self.friends.add(account)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Generate a token every time a new account object
    is created.
    """
    if created:
        Token.objects.create(user=instance)
