from django.db import models

# Create your models here.


class Admin(models.Model):
    ID = models.IntegerField()
    Name = models.CharField()
    Email = models.CharField()
    Password = models.CharField()


class Patient(models.Model):
    ID = models.IntegerField()
    Name = models.CharField()
    BirthDay = models.DateTimeField()
    WorkName = models.CharField()
    City = models.CharField()
    Phone = models.IntegerField(max_length=11)


class Doctor(models.Model):
    ID = models.IntegerField()
    Name = models.CharField()
    BirthDay = models.DateTimeField()
    WorkName = models.CharField()
    City = models.CharField()
    Phone = models.IntegerField(max_length=11)
    Special = models.CharField()


class Department(models.Model):
    Code = models.IntegerField()
    Name = models.CharField()

    # Multi value
    Appiontment = models.DateTimeField()


class ReservationTicket(models.Model):
    Code = models.IntegerField()
    PatientName = models.CharField()
    PatientDoctor = models.CharField()
    Department = models.CharField()
    Disease = models.CharField()
    State_of_treatement = models.BooleanField()
