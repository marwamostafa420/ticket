"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Admin.views import Dashboard, Ticket, admininfo, deletedepartment, deletepatient, department, doctor, editdepartment, patients, searchdepartment, searchpatient, updatedepartment, deleteDoc, addEditDoc, addEditPatient

from . import views
from Project.views import children, digestion, ear, eyes, gyn, heart, internal, kidney, oncology, radiology, showclinc, teeth, urology, reserve, forgetEmail, add_Feedback
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dashboard', Dashboard, name='Dashboard'),
    path('Dashboard/patient', patients, name='Dashboard/patient'),
    path('Dashboard/admin', admininfo, name='Dashboard/admin'),
    path('Dashboard/departments', department, name='Dashboard/departments'),
    path('Dashboard/doctors', doctor, name='Dashboard/doctors'),
    path('Dashboard/ticket', Ticket, name='Dashboard/ticket'),
    path('clinic/', children, name='children'),
    path('clinic1/', digestion, name='digestion'),
    path('clinic2/', ear, name='ear'),
    path('clinic3/', eyes, name='eyes'),
    path('clinic4/', gyn, name='gyn'),
    path('clinic5/', heart, name='heart'),
    path('clinic6/', internal, name='internal'),
    path('clinic7/', kidney, name='kidney'),
    path('clinic8/', oncology, name='oncology'),
    path('clinic9/', radiology, name='radiology'),
    path('clinic10/', teeth, name='teeth'),
    path('clinic11/', urology, name='urology'),
    path('reserve/', reserve, name='reserve'),


    path('', views.home, name='Home'),
    path('profile', views.profile),
    path('MoreServ/', views.more_serv, name='more_serv'),
    # path('SignUp', views.singup, name='signup'),


    path('Login', LoginView.as_view(
        template_name="LOGIN/index.html"), name='login'),

    path('logout', LogoutView.as_view(
        template_name='Home/home.html'), name='logout'),

    path('????????????', views.arabic, name='arabic'),
    path('??????????', views.ARsingup, name='ARsignup'),
    path('?????????? ????????????', views.ARlogin, name='ARlogin'),
    path('ticket', views.ticket, name='ticket'),
    path('forgetEmail', views.forgetEmail, name='forgetEmail'),

    # Dashboard Action
    path('delete/<depid>', deletedepartment, name="deletedepartment"),
    path('search_dep', searchdepartment, name="search_dep"),



    path('update/<id>', editdepartment, name='edit_department'),
    path('updatedepartment', updatedepartment, name='updatedepartment'),

    path('addPatient', addEditPatient, name='addPat'),
    path('EditPatient/<int:id>', addEditPatient, name='editPat'),
    path('deletepatient/<p_id>', deletepatient, name="deletepatient"),
    path('searchpatient', searchpatient, name='searchpatient'),

    path('showclinc/<id>', showclinc, name='showclinc'),

    path('deleteDoc/<int:id>', deleteDoc, name='deleteDoc'),
    path('addDoctor', addEditDoc, name='addDoc'),
    path('EditDoctor/<int:id>', addEditDoc, name='editDoc'),
    path('newfeedback', add_Feedback, name='newfeedback'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
