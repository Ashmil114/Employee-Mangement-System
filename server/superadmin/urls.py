from django.urls import path,include
from django.http import HttpResponse
from .views import AddDepartment,AddDesignation,DepartmentList,DesignationList
 
def Home(request):
    return HttpResponse("SuperAdmin")

urlpatterns = [
    path('',Home),
    path('department-list/',DepartmentList.as_view(),name='department-list'),       # [GET]
    path('designation-list/',DesignationList.as_view(),name='designation-list'),    # [GET]
    path('add-department/',AddDepartment.as_view(),name='add-department'),          # [POST] name
    path('add-designation/',AddDesignation.as_view(),name='add-designation'),       # [POST] name,priority
]