import os

from django.core.management.base import BaseCommand
from accounts.models import Account

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Account.objects.filter(username="admin").exists():
            Account.objects.create_superuser("admin", "admin@admin.com", "admin")