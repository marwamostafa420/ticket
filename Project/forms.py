from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class signupForm(UserCreationForm):
    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'username',
                  'password1', 'password2')
