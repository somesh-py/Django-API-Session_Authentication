from django.db import models

# Create your models here.

class Employee(models.Model):
    empid=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    contact=models.IntegerField(max_length=10)
    department=models.CharField(max_length=50)
    jobtype=models.CharField(max_length=50)
    address=models.CharField(max_length=50)