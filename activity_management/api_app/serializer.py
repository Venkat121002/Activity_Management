from activity_app.models import Task,ActivityLog,Remainder
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ActivitylogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'

class RemainderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remainder
        fields = '__all__'

