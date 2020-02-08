from rest_framework import routers
from app.viewsets import ActivityViewSet, ActivityListViewSet, ReminderViewSet, DueViewSet, ActionViewSet

router = routers.DefaultRouter()

router.register(r'activity', ActivityViewSet)
router.register(r'activitylist', ActivityListViewSet)
router.register(r'action', ActionViewSet)
router.register(r'reminder', ReminderViewSet)
router.register(r'due', DueViewSet)
