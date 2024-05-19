from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.core.cache import cache

from taskandtarget.models import Task
from .task_serializer import TaskSerializer

class TaskList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        cache_key = 'Task_list'
        data = cache.get(cache_key)
        
        if data is None:
            queryset = self.get_queryset()
            serializer = TaskSerializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60*15)  # Cache timeout set to 15 minutes
        
        return Response(data)