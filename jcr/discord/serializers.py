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
        opp = models.VolunteerOpportunity.objects.create(
            start_date=validated_data["date"],
            start_time=validated_data["time"],
            location=validated_data["location"],
            title=validated_data["title"],
            description=validated_data["desc"],
            event=validated_data["event"],
        )
        return opp

class VolunteerOpportunityWebhookEvent(serializers.Serializer):
    Parsed = VolunteerOpportunityPayload(required=False)
    Err = serializers.CharField(required=False)
    Text = serializers.CharField(required=False)

    def create(self, validated_data):
        parsed = validated_data.get("Parsed")
        if parsed:
            serializer = VolunteerOpportunityPayload(data=parsed)
            serializer.is_valid(raise_exception=True)
            return serializer.save()

        return True # Fail silently if no volunteer opps

class VolunteerOpportunityWebhookPayload(serializers.Serializer):
    eligibles = VolunteerOpportunityWebhookEvent(many=True, required=False)
    ineligibles = VolunteerOpportunityWebhookEvent(many=True, required=False)
    medicals = VolunteerOpportunityWebhookEvent(many=True, required=False)

    def create(self, validated_data):
        eligibles = validated_data.get("eligibles", [])
        if eligibles:
            serializer = VolunteerOpportunityWebhookEvent(data=eligibles, many=True)
            serializer.is_valid(raise_exception=True)
            return serializer.save()

        return []
