from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from police.models import User


class Crime(models.Model):
    OPEN = 'OPEN'
    CLOSE = 'CLOSE'
    PENDING = 'PENDING'
    CRIME_STATUS = [
        (OPEN, 'OPEN'),
        (CLOSE, 'CLOSE'),
        (PENDING, 'PENDING'),
    ]

    type = models.CharField(max_length=50)
    crime_status = models.CharField(
        max_length=50, choices=CRIME_STATUS, default=OPEN)
    court = models.CharField(max_length=255, blank=True, null=True)
    verdict = models.CharField(max_length=100, blank=True, null=True)
    crime_location = models.CharField(max_length=50, blank=True, null=True)
    date_of_crime = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    time_of_crime = models.TimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    statement = models.CharField(max_length=255, blank=True, null=True)
    police = models.ForeignKey(
        User, related_name='police', on_delete=models.CASCADE, blank=True, null=True)
    added_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.type


class Criminal(models.Model):
    # to create a field with a choice between male and female
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER = [
        (MALE, 'male'),
        (FEMALE, 'female'),
    ]

    WANTED = 'WANTED'
    NOT_WANTED = 'NOT_WANTED'
    STATUS = [
        (WANTED, 'wanted'),
        (NOT_WANTED, 'not_wanted'),
    ]

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    aliases = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    state_of_origin = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    hair_color = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    sex = models.CharField(max_length=50, choices=GENDER, default=MALE)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    wanted_status = models.CharField(
        max_length=50, choices=STATUS, default=NOT_WANTED)
    description = models.CharField(max_length=50, blank=True, null=True)
    foot_size = models.CharField(max_length=50, blank=True, null=True)
    place_of_arrest = models.CharField(max_length=255, blank=True, null=True)
    residence = models.CharField(max_length=255, blank=True, null=True)
    date_of_arrest = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    crime = models.ManyToManyField('Crime')

    def __str__(self):
        return self.first_name


class CriminalImage(models.Model):
    criminal = models.OneToOneField(
        Criminal, on_delete=models.CASCADE, blank=True, null=True)
    image1 = models.ImageField(
        upload_to='criminal_pics/', default='default1.jpg')
    image2 = models.ImageField(
        upload_to='criminal_pics/', default='default2.jpg')

    def __str__(self):
        return self.criminal.first_name


class FingerPrint(models.Model):
    # collection of the fingerprint templates of each ciminal. where each ciminal has 10 fingerprints
    right_thumb = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    right_index = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    right_middle = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    right_ring = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    right_pinky = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    left_thumb = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    left_index = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    left_middle = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    left_ring = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
    left_pinky = models.CharField(
        max_length=1000, blank=True, null=True, unique=True)
