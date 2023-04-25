from rest_framework.routers import SimpleRouter
from .views import VolunteerOpportunitySummaryViewSet

router = SimpleRouter()
router.register(r'opportunities', VolunteerOpportunitySummaryViewSet, basename='volunteer-opportunities')
urlpatterns = router.urls

