from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password','address','gender','dob']
        widgets = {
            "name" : forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control', 'required': 'required'}),
            "email" : forms.EmailField(attrs={'placeholder': 'Email', 'class': 'form-control', 'required': 'required'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'required': 'required'}),
            'dob' : forms.DateField(attrs={'placeholder': 'Date Of Birth', 'class': 'form-control', 'required': 'required'}),
        }