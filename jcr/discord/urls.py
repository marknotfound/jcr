from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'webhooks/opportunities', views.VolunteerOpportunityWebhook, basename='volunteer-opportunities-webhook')
router.register(r'opportunities', views.VolunteerOpportunities, basename='volunteer-opportunities')

urlpatterns = router.urls

