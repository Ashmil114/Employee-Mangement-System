from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.core.cache import cache

from taskandtarget.models import Task
from .task_serializer import TaskSerializer

from worker.models import Worker
from superadmin.models import Designation,Department

from worker.views import GetUser

# from rest_framework.authtoken.models import Token

class TaskList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    # queryset = Task.objects.all()
    queryset = Task.objects.select_related('assigned_to').all()
    serializer_class = TaskSerializer

    def list(self, request):
        cache_key = 'task_list'
        data = cache.get(cache_key)
        
        if data is None:
            queryset = self.get_queryset()
            serializer = TaskSerializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60*15)  # Cache timeout set to 15 minutes
        
        return Response(data)

class AddTask(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def post(self,request):
        title = request.data.get('title')
        deadline = request.data.get('deadline')
        status = request.data.get('status')
        user_id = request.data.get('user_id')
        token = request.data.get('token')
        
        try:
            res = GetUser(token=token)
            if res == True:
                super_admin = res
            else :
                super_admin = False
        except Exception as e:
            return Response({'error':str(e)})
            
        
        try :
            user = Worker.objects.get(pk=user_id)
        except Worker.DoesNotExist:
            return Response({'error':'User Not Exists'})
        
        try:
            if super_admin == True :
                priority = 1
                department_name ='all'
                designation_name = 'superadmin'
            else :
                try:
                    admin = GetUser(token=token)
                    print(admin)
                    
                    # priority = Designation.objects.get(name__iexact=assigned_by).priority 
                    designation_name = admin.designation.name
                    priority = admin.designation.priority
                    department_name = admin.department.name
                    # department_name =  Department.objects.get(name_iexact=department).name
                    # print(f'================{priority,department_name}=========')
                except Exception as e:
                    return Response({'error':str(e)})
        except:
            pass
        
        try :
            if department_name == 'all':
                pass
            else :
                if  user.department.name.lower() != department_name.lower():
                    return Response({'error':f'As Your  a {department_name}  {designation_name} You Cannot assign task for other department employees'})  
        except:
            pass
        
        
        try :
            if  user.designation.name.lower() == 'staff':
                pass
            elif user.designation.priority == priority:
                return Response({'error':'You Cannot assign task for same designation employees'})
            else:
                if  user.designation.priority < priority :
                    return Response({'error':'You Cannot assign task for higher designation employees'})
        except:
            pass 
        
        try :
            Task.objects.create(title=title,deadline=deadline,status=status,assigned_by=designation_name,assigned_to=user)
            return Response({'message':'Task Assigned'})
        except Exception as e:
            return Response({'error':str(e)})
        