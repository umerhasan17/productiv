from rest_framework import viewsets
from .models import Activity, ActivityList, Due, Reminder, Action
from .serializers import ActivitySerializer, ActivityListSerializer, DueSerializer, ReminderSerializer, ActionSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityListViewSet(viewsets.ModelViewSet):
    queryset = ActivityList.objects.all()
    serializer_class = ActivityListSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    
class DueViewSet(viewsets.ModelViewSet):
    queryset = Due.objects.all()
    serializer_class = DueSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer