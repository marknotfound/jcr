from http import HTTPStatus
import requests
from rest_framework import viewsets, response, mixins
from django.conf import settings
from . import serializers, models
from .messages import MessageGenerator


class VolunteerOpportunityWebhook(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.VolunteerOpportunityWebhookPayload(data=request.data)
        serializer.is_valid(raise_exception=True)
        instances = serializer.save()

        message = MessageGenerator.generate_volunteer_opportunities_message(instances)

        if message:
            SUPRESS_EMBEDS = 1 << 2
            requests.post(settings.NYRR_WEBHOOK, { "content": message, "flags": SUPRESS_EMBEDS })

        return response.Response(None, status=HTTPStatus.NO_CONTENT)

class VolunteerOpportunities(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.VolunteerOpportunity
    queryset = models.VolunteerOpportunity.objects.all()
