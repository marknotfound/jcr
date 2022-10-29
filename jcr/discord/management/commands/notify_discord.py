import requests
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        requests.post(
            settings.NYRR_WEBHOOK,
            {"content": "Build to fly.io completed"}
        )