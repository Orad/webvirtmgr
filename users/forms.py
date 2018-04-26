from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserInfoForm(ModelForm):
    phone_number = forms.CharField(max_length=10,required=False)

    class Meta:
        model = User
    	fields = ['first_name', 'last_name', 'email', 'phone_number']
         