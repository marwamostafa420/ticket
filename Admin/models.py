from datetime import datetime
from operator import mod
from socket import inet_aton
# from django.db import models
from datetime import datetime
from django.db import models
# Create your models here.


class Admin(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)



class Doctor(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    WorkName = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Phone = models.CharField(max_length=11)
    Special = models.CharField(max_length=100)

    see=models.ForeignKey(Admin,on_delete=models.PROTECT)



class Patient(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    BirthDay = models.DateTimeField()
    WorkName = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Phone = models.CharField(max_length=11)
    reserved =models.BooleanField(default=False)

    see=models.ForeignKey(Admin,on_delete=models.PROTECT)
    examin=models.ForeignKey(Doctor,on_delete=models.PROTECT)
    
    






class Department(models.Model):
    Code = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)

    # Multi value
    # Appiontment = models.DateTimeField()
    choose=models.OneToOneField(Patient,on_delete=models.PROTECT,null=False)
    work=models.OneToOneField(Doctor,on_delete=models.PROTECT)




class Appointment(models.Model):
    code=models.IntegerField(primary_key=True)
    dep_Id=models.IntegerField()
    day=models.CharField(max_length=10)

    time=models.ForeignKey(Department,on_delete=models.CASCADE)



class ReservationTicket(models.Model):
    Code = models.IntegerField(primary_key=True)
    PatientName = models.CharField(max_length=100)
    PatientDoctor = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Disease = models.CharField(max_length=100)

    # 0 ---> على حسابك
    # 1--> على نفقه الدوله
    State_of_treatement = models.BooleanField(default=False)

    write=models.OneToOneField(Doctor,on_delete=models.PROTECT)
    have=models.OneToOneField(Patient,on_delete=models.PROTECT)
