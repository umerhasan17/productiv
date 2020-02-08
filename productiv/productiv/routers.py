from rest_framework import routers
from article.viewsets import ActivityViewSet

router = routers.DefaultRouter()
router.register(r’activity’, ActivityViewSet)