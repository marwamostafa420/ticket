import datetime
import os
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" %(timenow,old_filename)
    return os.path.join("upload/",filename)


class Department(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to=filepath, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    Days = models.CharField(max_length=255)
    Days2 = models.CharField(max_length=255, null=True)
    rate = models.IntegerField(validators=([MinValueValidator(0), MaxValueValidator(5)]))
    def __str__(self) -> str:
        return self.name

class Jobtitles(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    name = models.CharField(max_length=255)


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    Phone = models.CharField(max_length=11)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Patient(models.Model):
    National_num = models.CharField(max_length=200)
    Name = models.CharField(max_length=100)
    BirthDay = models.DateTimeField()
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    Phone = models.CharField(max_length=11)
    reserved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class ticket(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Pat = models.ForeignKey(Patient, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    startdate = models.DateTimeField(null=True)
    enddate = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class feedback(models.Model):
    Feedback = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Appointment(models.Model):
    dep_Id = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    # time=models.ForeignKey(Department,on_delete=models.CASCADE)


class ReservationTicket(models.Model):
    PatientName = models.CharField(max_length=100)
    PatientDoctor = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Disease = models.CharField(max_length=100)

    # 0 ---> على حسابك
    # 1--> على نفقه الدوله
    State_of_treatement = models.BooleanField(default=False)

    write = models.OneToOneField(Doctor, on_delete=models.PROTECT)
    have = models.OneToOneField(Patient, on_delete=models.PROTECT)
