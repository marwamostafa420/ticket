import os
from django.shortcuts import redirect, render
from django.contrib import messages
from Admin.forms import clincform,  patientform, doctorForm
from Admin.models import Department, Patient, Doctor, ticket

# Create your views here.


def Dashboard(request):
    Departmentcount = Department.objects.count()
    patientscount = Patient.objects.count()
    doctorscount = Doctor.objects.count()
    ticketcount = ticket.objects.count()
    return render(request, 'Dashbord.html', {'deps': Departmentcount, 'pat': patientscount, 'doc': doctorscount, 'ticket': ticketcount})


def admininfo(request):
    return render(request, 'admin.html')


def department(request):
    deps = Department.objects.all()

    form = clincform(request.POST or None, request.FILES or None)
    context = {'deps': deps, 'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, "A Clincal Has Been Added Succesfully ")
        return redirect('Dashboard/departments')
    return render(request, 'departments.html', context)


def doctor(request):
    doctor = Doctor.objects.all()
    messages.success(request, "A Doctro Has Been Deleted Succesfully ")
    return render(request, 'doctors.html', {'doctor': doctor})


def addEditDoc(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = doctorForm()
        else:
            doc = Doctor.objects.get(pk=id)
            form = doctorForm(instance=doc)
        return render(request, 'edit_doctor.html', {'form': form})

    else:
        if id == 0:
            form = doctorForm(request.POST)
        else:
            doc = Doctor.objects.get(pk=id)
            form = doctorForm(request.POST, instance=doc)

        if form.is_valid():
            form.save()
    return redirect('Dashboard/doctors')


def deleteDoc(request, id):
    item = Doctor.objects.get(pk=id)
    item.delete()
    messages.success(request, "A Doctor Has Been Deleted Succesfully ")
    return redirect('Dashboard/doctors')


def patients(request):
    # city=City.objects.get(pk=city_id)
    pat = Patient.objects.all()
    return render(request, 'patients.html', {'pat': pat})


def addEditPatient(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = patientform()
        else:
            pat = Patient.objects.get(pk=id)
            form = patientform(instance=pat)
        return render(request, 'editpatient.html', {'form': form})
    else:
        if id == 0:
            form = patientform(request.POST)
        else:
            pat = Patient.objects.get(pk=id)
            form = patientform(request.POST, instance=pat)
        if form.is_valid():
            form.save()
    return redirect('Dashboard/patient')


def Ticket(request):
    return render(request, 'ticket.html')


# Dashboard action
def deletedepartment(request, depid):
    dep = Department.objects.get(pk=depid)
    if len(dep.img) > 0:
        os.remove(dep.img.path)
    dep.delete()
    messages.success(request, "A Clincal Has Been Deleted Succesfully ")
    return redirect('Dashboard/departments')


def searchdepartment(request):
    # item = Items()
    if request.method == "POST":
        key = request.POST.get('search')
        form = clincform(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "A Clincal Has Been Added Succesfully ")
        res = Department.objects.filter(name__icontains=key)
        return render(request, "search_dep.html", {"departments": res, 'form': form})
    else:
        return render(request, "search_dep.html", {})


def editdepartment(request, id):
    data = Department.objects.get(pk=id)
    context = {'data': data}
    return render(request, 'edit_department.html', context)


def updatedepartment(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        startday = request.POST.get('startday')
        endday = request.POST.get('endday')
        # img =request.POST.get('img')
        rate = request.POST.get('rate')
        price = request.POST.get('price')

        data = Department.objects.get(pk=id)
        # if len(request.FILES) != 0:
        #     if len(data.img) > 0:
        #         os.remove(data.img.path)
        data.img = request.FILES['img']
        data.name = name
        data.desc = desc
        data.Days = startday
        data.Days2 = endday
        data.rate = rate
        data.price = price
        data.save()
        messages.success(request, 'Clical Updated Succesfuly')
        return redirect("Dashboard/departments")
    return render(request, 'departments.html')


def deletepatient(request, p_id):
    item = Patient.objects.get(id=p_id)
    item.delete()
    messages.success(request, "A Patient Has Been Deleted Succesfully ")
    return redirect('Dashboard/patient')


def searchpatient(request):
    if request.method == 'POST':
        key = request.POST.get('search')
        res = Patient.objects.filter(Name__icontains=key)
        return render(request, "searchpatient.html", {"patients": res})
    else:
        return render(request, "searchpatient.html", {})
