from django.db import models
from django.contrib.auth.models import User
from superadmin.models import Department,Designation
import uuid

class Worker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile',editable=False)
    phone = models.CharField(max_length=10,null=False,unique=True,blank=False)
    name = models.CharField(max_length=150,blank=False,null=False)
    email = models.EmailField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,default='staff')
    is_admin = models.BooleanField(null=False,blank=False,default=False)
    
    
    def __str__(self):
        return self.user.username
    