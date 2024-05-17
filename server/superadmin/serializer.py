from rest_framework import serializers
from .models import Department,Designation

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name','created')

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ('name','priority')