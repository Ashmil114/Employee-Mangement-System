from django.urls import path,include
from django.http import HttpResponse
from rest_framework.authtoken import views

def Home(request):
    return HttpResponse("Worker")

urlpatterns = [
    path('',Home),
    path('worker-login/', views.obtain_auth_token), # [POST] username(phone number) , password
    
]