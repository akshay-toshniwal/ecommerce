from dataclasses import fields
from queue import Empty
from allauth.account.forms import SignupForm
from django import forms
from .models import *
from django.forms.widgets import NumberInput  

class CustomSignupForm(SignupForm):
    CHOICES=[('1','Male'),
         ('2','Female'),
         ('3','Other')]
    name = forms.CharField(max_length=25, label='Name')
    username = forms.CharField(max_length=25, label='UserName')
    dob = forms.DateField(widget = NumberInput(attrs={'type':'date'}),label='Date Of Birth')
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),label='Address')
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.Select)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.username = self.cleaned_data['username']
        user.dob = self.cleaned_data['dob']
        user.gender = self.cleaned_data['gender']
        user.address = self.cleaned_data['address']
        user.save()
        return user

class EditProfile(forms.ModelForm):
    class Meta:
        CHOICES=[('1','Male'),
         ('2','Female'),
         ('3','Other')]
        model = User
        fields = ['name','username','address','dob','gender']
        widgets = {
            "name" : forms.TextInput(attrs = {'placeholder': 'Name', 'class': 'form-control', 'required': 'required'}),
            "username" : forms.TextInput(attrs = {'placeholder': 'UserName', 'class': 'form-control', 'required': 'required'}),
            "address" : forms.Textarea(attrs = {'rows':3, 'placeholder': 'Address', 'class': 'form-control', 'required': 'required'}),
            "dob" : forms.NumberInput(attrs = {'type':'date','placeholder': 'Date Of Birth', 'class': 'form-control', 'required': 'required'}),
            "gender" : forms.Select(choices = CHOICES,attrs = {'class': 'form-control', 'required': 'required'})
        }
        