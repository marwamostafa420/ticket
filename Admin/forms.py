
from django import forms
from .models import Department
class clincform(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class':'form-control'}),
            'desc': forms.Textarea(attrs={'class':'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'Days': forms.TextInput(attrs={'class':'form-control'}),
            'Days2': forms.TextInput(attrs={'class':'form-control'}),   
            'price': forms.TextInput(attrs={'class':'form-control','placeholder':'Price Per LE'}),
        }