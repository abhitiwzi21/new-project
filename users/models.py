from django.db import models
import uuid




class Employee(models.Model):
    reference_id= models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=50,default=None)
    address = models.CharField(max_length=500,default=None)
    amount = models.IntegerField(default=10)
    trans_type = models.IntegerField(default=None)
    status=models.CharField(max_length=50,default=None)
    trans_id=models.UUIDField(default=uuid.uuid4)
    trans_no=models.UUIDField(default=uuid.uuid4)
    date=models.DateTimeField(auto_now=True)





