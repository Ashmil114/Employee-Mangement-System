from rest_framework import serializers
from worker.models import Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta :
        model = Worker
        fields = '__all__'
        depth = 2