import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.db import transaction

from police.models import User

from .models import Criminal, Crime


class NewCriminalForm(forms.ModelForm):
    class Meta:
        model = Criminal
        fields = ('first_name', 'middle_name', 'last_name', 'aliases', 'wanted_status', 'email',
                  'date_of_birth', 'sex', 'hair_color', 'height', 'weight', 'foot_size', 'occupation',
                  'phone_number', 'nationality', 'state_of_origin', 'residence', 'description',
                  'place_of_arrest', 'date_of_arrest', 'image1', 'image2', 'crime')
        widgets = {
            'date_of_birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'date_of_arrest': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }


class NewCrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ['type', 'crime_status', 'court', 'verdict', 'crime_location', 'date_of_crime',
                  'time_of_crime', 'statement', 'police']
        widgets = {
            'date_of_crime': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),        
            'time_of_crime': forms.TimeInput(format=('%H:%M'), attrs={'class': 'form-control', 'placeholder': 'Select time', 'type': 'time'}),        

            }
