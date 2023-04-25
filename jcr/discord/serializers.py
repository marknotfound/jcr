from rest_framework import serializers
from .models import VolunteerOpportunitySummary

class VolunteerOpportunitySerializer(serializers.ModelSerializer):
    npo_eligible = serializers.IntegerField(required=True)

    class Meta:
        model = VolunteerOpportunitySummary
        fields = (
            "npo_eligible",
            "created",
        )

