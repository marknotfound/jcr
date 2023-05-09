import logging
from datetime import timedelta
from django.utils import timezone
from django.core.management import BaseCommand

from discord.models import VolunteerOpportunity

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        cutoff = timezone.now() - timedelta(hours=24)
        queryset = VolunteerOpportunity.objects.filter(created__lte=cutoff)
        queryset.delete()
