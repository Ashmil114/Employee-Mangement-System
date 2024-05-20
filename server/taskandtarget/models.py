from django.db import models
import uuid
from worker.models import Worker

STATUS_CHOICE =(
    ('pending','pending'),
    ('completed','completed'),
    ('overdue','overdue')
)
# ASSIGNEDBY_CHOICE = (
#     ('superadmin','superadmin'),
#     ('admin','admin')
# )

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(blank=False,null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default='pending')
    assigned_by = models.CharField(max_length=20,default='superadmin')
    assigned_to = models.ForeignKey(Worker,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    