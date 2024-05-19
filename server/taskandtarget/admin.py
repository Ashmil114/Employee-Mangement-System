from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title','assigned_by','assigned_to','created','deadline','status')
    
admin.site.register(Task,TaskAdmin)