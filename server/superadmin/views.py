from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Department,Designation
from .serializer import DepartmentSerializer,DesignationSerializer

from django.core.cache import cache

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class SuperAdminLogin(APIView):
    ...


class DepartmentList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
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
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
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
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
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
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    
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

class UpdateDepartment(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def put(self, request, pk, format=None):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        try:
            department = Department.objects.get(pk=pk)
            department.delete()
            return Response("Department Deleted")
        except Department.DoesNotExist:
            return Response('Department Not Found this Name')
        

class UpdateDesignation(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def put(self, request, pk, format=None):
        designation = Designation.objects.get(pk=pk)
        serializer = DesignationSerializer(designation, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        try:
            designation = Designation.objects.get(pk=pk)
            designation.delete()
            return Response("Designation Deleted")
        except Designation.DoesNotExist:
            return Response('Designation Not Found this Name')