import re
from rest_framework import serializers
from . import models

class VolunteerOpportunity(serializers.ModelSerializer):
    class Meta:
        model = models.VolunteerOpportunity
        fields = "__all__"

class VolunteerOpportunityPayload(serializers.Serializer):
    date = serializers.CharField(required=True)
    time = serializers.CharField(required=True)
    location = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    desc = serializers.CharField(required=True)
    event = serializers.CharField(required=True)

    def create(self, validated_data):
        opp, created = models.VolunteerOpportunity.objects.update_or_create(
            event=validated_data["event"],
            title=validated_data["title"],
            defaults={
                "start_date": validated_data["date"],
                "start_time": validated_data["time"],
                "location": validated_data["location"],
                "description": validated_data["desc"],
            },
        )
        return opp, created

class VolunteerOpportunityWebhookEvent(serializers.Serializer):
    Parsed = VolunteerOpportunityPayload(required=False)
    Err = serializers.CharField(required=False)
    Text = serializers.CharField(required=False)

    def create(self, validated_data):
        parsed = validated_data.get("Parsed")
        opp = created = None
        if parsed:
            serializer = VolunteerOpportunityPayload(data=parsed)
            serializer.is_valid(raise_exception=True)
            description = serializer.validated_data["desc"]
            not_plus_one = "not\s?+a?\s?+9?\+1"
            if not re.search(not_plus_one, description):
                opp, created = serializer.save()

        return opp if created else True # Fail silently if no volunteer opps

class VolunteerOpportunityWebhookPayload(serializers.Serializer):
    eligibles = VolunteerOpportunityWebhookEvent(many=True, required=False)
    ineligibles = VolunteerOpportunityWebhookEvent(many=True, required=False)
    medicals = VolunteerOpportunityWebhookEvent(many=True, required=False)

    def create(self, validated_data):
        eligibles = validated_data.get("eligibles", [])
        if eligibles:
            serializer = VolunteerOpportunityWebhookEvent(data=eligibles, many=True)
            serializer.is_valid(raise_exception=True)
            return [i for i in serializer.save() if isinstance(i, models.VolunteerOpportunity)]

        return []
