from django.contrib import admin

# Register your models here.

# from .models import Admin, Patient, Doctor, Department, ReservationTicket


# admin.site.register((Admin, Patient, Doctor, Department, ReservationTicket,))


from .models import Admin , Patient,Doctor,Department,ReservationTicket

admin.site.register((Admin , Patient,Doctor,Department,ReservationTicket))
