from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    CHOICES=[('1','Male'),
         ('2','Female'),
         ('3','Other')]
    name = forms.CharField(max_length=25, label='Name')
    username = forms.CharField(max_length=25, label='UserName')
    dob = forms.DateField(label='Date Of Birth')
    address = forms.CharField(widget=forms.Textarea,label='Address')
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.username = self.cleaned_data['username']
        user.dob = self.cleaned_data['dob']
        user.gender = self.cleaned_data['gender']
        user.address = self.cleaned_data['address']
        user.save()
        return user