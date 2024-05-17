from django.urls import path,include
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Server Running...")

urlpatterns = [
    path('',Home),
    path('superadmin/',include('superadmin.urls')),
    path('deptadmin/',include('deptadmin.urls')),
    path('worker/',include('worker.urls')),
    
]