from django.urls import path,include
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Worker")

urlpatterns = [
    path('',Home)
    
]