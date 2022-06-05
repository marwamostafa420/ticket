from django.shortcuts import redirect, render

from Admin.forms import clincform
from Admin.models import Department,Patient,Doctor,ticket

# Create your views here.
def Dashboard(request):
    Departmentcount = Department.objects.count()
    patientscount = Patient.objects.count()
    doctorscount = Doctor.objects.count()
    ticketcount  = ticket.objects.count()
    return render(request,'Dashbord.html',{'deps':Departmentcount,'pat':patientscount,'doc':doctorscount,'ticket':ticketcount})
def admininfo(request):
    return render(request,'admin.html')


def department(request):
    deps = Department.objects.all()

    form = clincform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('Dashboard/departments')
    
    return render(request,'departments.html',{'deps':deps,'form':form})


def doctor(request):
    return render(request,'doctors.html')


def patients(request):
    return render(request,'patients.html')


def Ticket(request):
    return render(request,'ticket.html')


# Dashboard action
def deletedepartment(request,depid):
    dep = Department.objects.get(pk=depid)
    dep.delete()
    return redirect('Dashboard/departments')

def searchdepartment(request):
    # item = Items()
    if request.method == "POST":
        key = request.POST.get('search')
        
        res = Department.objects.filter(name__icontains = key)
        return render(request,"search_dep.html",{"departments":res})
    else:
        return render(request,"search_dep.html",{})       
    
