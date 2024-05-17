from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Department,Designation
from .serializer import DepartmentSerializer,DesignationSerializer

from django.core.cache import cache

class SuperAdminLogin(APIView):
    ...


class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request):
        cache_key = 'department_list'
        data = cache.get(cache_key)
        
        if data is None:
            queryset = self.get_queryset()
            serializer = DepartmentSerializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60*15)  # Cache timeout set to 15 minutes
        
        return Response(data)

class DesignationList(generics.ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

    def list(self, request):
        cache_key = 'designation_list'
        data = cache.get(cache_key)
        
        if data is None:
            queryset = self.get_queryset()
            serializer = DesignationSerializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60*15)  # Cache timeout set to 15 minutes
        
        return Response(data)

class AddDepartment(APIView):
    def post(self, request):
        name = request.data.get('name')
        if not name:
            return Response({'error': 'Name is required'}, status=400)

        try:
            dept = Department.objects.get(name__iexact=name)
            return Response({'error': f'Department with {name} name already exists'}, status=400)
        except Department.DoesNotExist:
            pass

        try:
            Department.objects.create(name=name)
            return Response({'message': f'{name} Department Created'}, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class AddDesignation(APIView):
    def post(self, request):
        name = request.data.get('name')
        priority = request.data.get('priority')
        if not name or not priority:
            return Response({'error': 'Name and priority are required'}, status=400)

        try:
            des = Designation.objects.get(name__iexact=name)
            return Response({'error': f'Designation with {name} name already exists'}, status=400)
        except Designation.DoesNotExist:
            pass

        try:
            Designation.objects.create(name=name,priority=priority)
            return Response({'message': f'{name} Designation Created'}, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=500)