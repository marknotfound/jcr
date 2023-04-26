from http import HTTPStatus
from rest_framework import viewsets, response, mixins
from . import serializers, models


class VolunteerOpportunityWebhook(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.VolunteerOpportunityWebhookPayload(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(None, status=HTTPStatus.NO_CONTENT)

class VolunteerOpportunities(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.VolunteerOpportunity
    queryset = models.VolunteerOpportunity.objects.all()
