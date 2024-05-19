from django.contrib import admin
from .models import Department,Designation

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id','name','priority')

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Designation,DesignationAdmin)
