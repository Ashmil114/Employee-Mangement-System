from django.contrib import admin
from .models import Worker

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id','phone','name','department','designation')

admin.site.register(Worker,WorkerAdmin)