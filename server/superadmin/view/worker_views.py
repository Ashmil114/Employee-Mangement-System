from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from django.core.cache import cache

from worker.models import Worker
from django.contrib.auth.models import User
from superadmin.models import Department,Designation

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from superadmin.view.worker_serializer import WorkerSerializer

class WorkerList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def list(self, request):
        cache_key = 'Worker_list'
        data = cache.get(cache_key)
        
        if data is None:
            queryset = self.get_queryset()
            serializer = WorkerSerializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60*15)  # Cache timeout set to 15 minutes
        
        return Response(data)

class AddWorker(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    
    def post(self,request):
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')
        department = request.data.get('department')
        designation = request.data.get('designation')
        is_admin = request.data.get('is_admin')
        password = request.data.get('password')
        
        
            
        try:
            user_obj = User.objects.get(username=phone)
        except User.DoesNotExist:
            user_obj = User.objects.create(username=phone)
            user_obj.set_password(password)
            user_obj.save()

        try:
            dept_obj = Department.objects.get(name__iexact=department)
        except Department.DoesNotExist:
            return Response({'error':f'No Department in name of {department}'})
        
        try:
            desig_obj = Designation.objects.get(name__iexact=designation)
        except Designation.DoesNotExist:
            return Response({'error':f'No Designation in name of {designation}'})
        
        try:
            Worker.objects.get(phone=phone)
            return Response({'error':f'Employee Already added on {phone} number'})
        except Worker.DoesNotExist:
            pass
        
        try:
            Worker.objects.get(department=dept_obj,designation=desig_obj,is_admin=True)
            return Response({'error':f'Already have a {designation} in {department}'})
        except Worker.DoesNotExist:
            pass
        
        try :
            user = Worker.objects.create(user=user_obj,phone=phone,name=name,email=email,department=dept_obj,designation=desig_obj,is_admin=is_admin)
            return Response({'message':'Employee Added'})
        except Exception as e:
            return Response ({'error':str(e)})

class ViewUpdateWorker(APIView):
    def get(self, request, pk, format=None):
        try:
            _data = Worker.objects.get(pk=pk)
            serializer = WorkerSerializer(_data)
            return Response(serializer.data)
        except Worker.DoesNotExist:
            return Response('Employee Not Found this Name')
    
    def put(self, request, pk, format=None):
        worker = Worker.objects.get(pk=pk)
        serializer = WorkerSerializer(worker, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        try:
            worker = Worker.objects.get(pk=pk)
            user = User.objects.get(username=worker.phone)
            worker.delete()
            user.delete()
            return Response("Worker Deleted")
        except Worker.DoesNotExist:
            return Response('Worker Not Found this Name')