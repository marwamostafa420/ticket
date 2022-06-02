from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import signupForm
# Home Page


def home(request):
    return render(request, "Home/home.html")


def children(request):
    return render(request, "clinic/children.html")


def digestion(request):
    return render(request, "clinic/digestion.html")


def ear(request):
    return render(request, "clinic/ear.html")


def eyes(request):
    return render(request, "clinic/eyes.html")


def gyn(request):
    return render(request, "clinic/gyn.html")


def heart(request):
    return render(request, "clinic/heart.html")


def internal(request):
    return render(request, "clinic/internal.html")


def kidney(request):
    return render(request, "clinic/kidney.html")


def oncology(request):
    return render(request, "clinic/oncology.html")


def radiology(request):
    return render(request, "clinic/radiology.html")


def teeth(request):
    return render(request, "clinic/teeth.html")


def urology(request):
    return render(request, "clinic/urology.html")


def profile(request):
    return render(request, 'Profile/profile.html')


def reserve(request):
    return render(request, "reservation/reserv.html")


def more_serv(request):
    return render(request, 'MoreServ/moreServ.html')


def arabic(request):
    return render(request, "Arabic/arabic.html")


def ARsingup(request):
    return render(request, "LOGIN/arabic/index2.html")


def ARlogin(request):
    return render(request, "LOGIN/arabic/index.html")


def ticket(request):
    return render(request, "Ticket/index.html")
