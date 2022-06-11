
from django import forms
from .models import Department, Patient, Doctor, feedback


class clincform(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'Days': forms.TextInput(attrs={'class': 'form-control'}),
            'Days2': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per LE'}),
        }


class patientform(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'BirthDay': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(patientform, self).__init__(*args, **kwargs)


class doctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
