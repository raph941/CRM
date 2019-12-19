import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.db import transaction

from police.models import User

from .models import Criminal, Crime, FingerPrint
from .Choices import *

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
        fields = ['type', 'crime_status', 'victim', 'police', 'country_of_crime', 'state_of_crime', 'local_gov_area',
                  'city_of_crime', 'date_of_crime', 'time_of_crime', 'statement', 'verdict', 'court' ]
                  
        widgets = {
            'date_of_crime': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),        
            'time_of_crime': forms.TimeInput(format=('%H:%M'), attrs={'class': 'form-control', 'placeholder': 'Select time', 'type': 'time'}),        

            }


class FingerprinttemplateForm(forms.ModelForm):
    class Meta:
        model = FingerPrint
        fields = ['criminal', 'right_thumb', 'right_index', 'right_middle', 'right_ring', 'right_pinky',
                    'left_thumb', 'left_index', 'left_middle', 'left_ring', 'left_pinky'] 


class SelectStateForAnalysisForm(forms.Form):
    select_state = forms.ChoiceField( choices=STATE, required=True, 
        label="Select State for Crime Analysis ", 
        initial=None, help_text="Criminal dtata available only for Plateau State at the moment")