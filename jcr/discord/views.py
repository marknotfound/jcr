from rest_framework import viewsets
from .models import VolunteerOpportunitySummary
from .serializers import VolunteerOpportunitySerializer

class VolunteerOpportunitySummaryViewSet(viewsets.ModelViewSet):
    queryset = VolunteerOpportunitySummary.objects.all()
    serializer_class = VolunteerOpportunitySerializer
