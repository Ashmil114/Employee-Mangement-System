from rest_framework import serializers
from taskandtarget.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta :
        model = Task
        fields = '__all__'
        depth = 2