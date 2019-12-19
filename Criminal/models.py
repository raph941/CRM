from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from police.models import User
from .Choices import *


class Crime(models.Model):
    type = models.CharField(max_length=50)
    crime_status = models.CharField(
        max_length=50, choices=CRIME_STATUS, default=OPEN)
    police = models.ForeignKey(
        User, related_name='police', on_delete=models.CASCADE, blank=True, null=True)
    court = models.CharField(max_length=255, blank=True, null=True)
    victim = models.CharField( max_length=50, blank=True, null=True)
    verdict = models.CharField(max_length=100, blank=True, null=True)
    country_of_crime = models.CharField(max_length=50, blank=True, null=True)
    state_of_crime = models.CharField(max_length=50, choices=STATE, blank=True, null=True)
    local_gov_area = models.CharField(max_length=50, choices=PLATEAU_LGA, blank=True, null=True)
    city_of_crime = models.CharField(max_length=50, blank=True, null=True)
    date_of_crime = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    time_of_crime = models.TimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    statement = models.CharField(max_length=255, blank=True, null=True) 
    
    date_added = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'case no:{ self.pk }, { self.type }'


class Criminal(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    aliases = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    hair_color = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    sex = models.CharField(max_length=50, choices=GENDER, default=MALE)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    wanted_status = models.CharField(
        max_length=50, choices=STATUS, default=NOT_WANTED)
    description = models.CharField(max_length=50, blank=True, null=True)
    state_of_origin = models.CharField(max_length=50, choices=STATE, null=True, blank=True)
    foot_size = models.CharField(max_length=50, blank=True, null=True)
    place_of_arrest = models.CharField(max_length=255, blank=True, null=True)
    residence = models.CharField(max_length=255, blank=True, null=True)
    date_of_arrest = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    image1 = models.ImageField(
        upload_to='criminal_pics/', default='default1.jpg')
    image2 = models.ImageField(
        upload_to='criminal_pics/', default='default2.jpg')
    
    crime = models.ManyToManyField('Crime')

    def __str__(self):
        return self.first_name



class FingerPrint(models.Model):
    # collection of the fingerprint templates of each ciminal. where each ciminal has 10 fingerprints
    criminal = models.ForeignKey('Criminal', related_name='criminal_print', on_delete=models.CASCADE, null=True)
    right_thumb = models.FileField(upload_to='documents/', blank=True, null=True)
    right_index = models.FileField(upload_to='documents/', blank=True, null=True)
    right_middle = models.FileField(upload_to='documents/', blank=True, null=True)
    right_ring = models.FileField(upload_to='documents/', blank=True, null=True)
    right_pinky = models.FileField(upload_to='documents/', blank=True, null=True)
    left_thumb = models.FileField(upload_to='documents/', blank=True, null=True)
    left_index = models.FileField(upload_to='documents/', blank=True, null=True)
    left_middle = models.FileField(upload_to='documents/', blank=True, null=True)
    left_ring = models.FileField(upload_to='documents/', blank=True, null=True)
    left_pinky = models.FileField(upload_to='documents/', blank=True, null=True)
