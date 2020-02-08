from rest_framework import serializers
from .models import Activity, Action, Reminder, Due, ActivityList

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityList
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

class DueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Due
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'