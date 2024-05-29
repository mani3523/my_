from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text="Enter your email",required=False)
    firstname = forms.CharField(help_text="Enter your firstname",required=True)
    middlename = forms.CharField(help_text="Enter your middlename(optional)",required=False)
    lastname = forms.CharField(help_text="Enter your lastname",required=True)
    class Meta:
        model = User
        fields = ['username','email','firstname','middlename','lastname','password1', 'password2']
        
'''      
class ForgetForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
'''