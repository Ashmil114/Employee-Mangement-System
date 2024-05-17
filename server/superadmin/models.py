from django.db import models
import uuid


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150,blank=False,null=False)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Designation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150,blank=False,null=False)
    priority = models.IntegerField(null=False,blank=False)
    
    def __str__(self):
        return self.name

