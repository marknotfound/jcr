from django.db import models
from django_extensions.db.models import TimeStampedModel


class ScrapedRace(TimeStampedModel):
    scraper = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)
    start_date = models.CharField(max_length=255, blank=True)
    start_time = models.CharField(max_length=255, blank=True)
    raw = models.JSONField(default=dict)


class VolunteerOpportunity(TimeStampedModel):
    start_date = models.CharField(max_length=255, blank=True)
    start_time = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    event = models.CharField(max_length=255, blank=True)
