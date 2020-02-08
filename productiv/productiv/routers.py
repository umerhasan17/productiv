from rest_framework import routers
from app.viewsets import ActivityViewSet

router = routers.DefaultRouter()

router.register(r'activity', ActivityViewSet)