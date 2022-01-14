from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=30, blank =False, default="")
    address=models.CharField(max_length=50,blank =False, default="")
    phone=models.IntegerField()
    email=models.EmailField(max_length=30,blank =False, default="")
    
class student(models.Model):
    first_name = models.CharField(max_length=30, blank =False, default="")
    last_name = models.CharField(max_length=30, blank =False, default="")
    date_of_birth=models.DateField(blank =False, default="")
    phone=models.BigIntegerField()
    grade=models.IntegerField()
    email=models.EmailField(max_length=30,blank =False, default="")
    
