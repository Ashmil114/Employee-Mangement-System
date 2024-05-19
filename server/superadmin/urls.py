from django.urls import path,include
from django.http import HttpResponse
from .views import AddDepartment,AddDesignation,DepartmentList,DesignationList,UpdateDepartment,UpdateDesignation
from superadmin.view.worker_views import AddWorker,WorkerList,ViewUpdateWorker
from superadmin.view.task_views import TaskList

def Home(request):
    return HttpResponse("SuperAdmin")

urlpatterns = [
    path('',Home),
    path('department-list/',DepartmentList.as_view(),name='department-list'),                       # [GET]
    path('designation-list/',DesignationList.as_view(),name='designation-list'),                    # [GET]
    path('add-department/',AddDepartment.as_view(),name='add-department'),                          # [POST] name
    path('add-designation/',AddDesignation.as_view(),name='add-designation'),                       # [POST] name,priority
    path('update-department/<slug:pk>',UpdateDepartment.as_view(),name='update-department'),        # [PUT] name  # [DELETE]
    path('update-designation/<slug:pk>',UpdateDesignation.as_view(),name='update-designation'),     # [PUT] name,priority # [DELETE]
    
    
    # WORKER ROUTES
    path('worker-list/',WorkerList.as_view(),name='worker-list'),                                   # [GET]
    path('add-worker/',AddWorker.as_view(),name='add-worker'),                                      # [POST] name,phone,email,department,designation,is_admin ,password
    path('view-update-worker/<slug:pk>',ViewUpdateWorker.as_view(),name='view-update-worker'),      # [GET] # [PUT] name,phone,email,department,designation,is_admin ,password # [DELETE]
    
    
    # TASK ROUTES
    path('task-list/',TaskList.as_view(),name='task-list'),                                         # [GET]
    
]