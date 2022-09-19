
from dataclasses import fields
from . models import *
from django import forms

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name','email','address','mobile_no']
    

