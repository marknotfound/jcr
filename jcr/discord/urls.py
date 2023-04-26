from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'webhooks/opportunities/', views.VolunteerOpportunityWebhook, basename='volunteer-opportunities')

urlpatterns = router.urls

