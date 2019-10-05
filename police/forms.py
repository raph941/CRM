import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from police.models import User

from .models import PoliceProfile


#begining of user creation forms   
class PoliceCreationForm(UserCreationForm):
    first_name = forms.CharField( max_length=30, required=False)
    last_name = forms.CharField( max_length=30, required=False)
    email = forms.EmailField(max_length = 254, required=False, help_text='enter a valid email address.')
    police_id = forms.CharField( max_length=30, required=True, )
    phone_number = forms.CharField( max_length=30, required=False)
    nationality = forms.CharField( max_length=30, required=False)
    state = forms.CharField( max_length=30, required=False)
    city = forms.CharField( max_length=30, required=False)
    profile_pic = forms.ImageField(max_length=254, required=False)
    
    class Meta:
        model = User
        User.is_police = True
        fields = ('username', 'first_name', 'last_name', 'email', 'police_id', 'phone_number',
                  'nationality', 'state', 'city', 'profile_pic', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = PoliceProfile
        fields = ('police_id', 'phone_number', 'nationality', 'state', 'city', 'profile_pic')


class AdminPoliceCreationForm(UserCreationForm):
    first_name = forms.CharField( max_length=30, required=False)
    last_name = forms.CharField( max_length=30, required=False)
    email = forms.EmailField(max_length = 254, required=False, help_text='inform a valid email address.')
    police_id = forms.CharField( max_length=30, required=True, )
    phone_number = forms.CharField( max_length=30, required=False)
    nationality = forms.CharField( max_length=30, required=False)
    state = forms.CharField( max_length=30, required=False)
    city = forms.CharField( max_length=30, required=False)
    profile_pic = forms.ImageField(max_length=254, required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'police_id', 'phone_number',
                  'nationality', 'state', 'city', 'profile_pic', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin_police = True
        if commit:
            user.save()
        return user
