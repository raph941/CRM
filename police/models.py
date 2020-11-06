from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class User(AbstractUser):
    is_police = models.NullBooleanField(default=False, db_index=True)
    is_admin_police = models.NullBooleanField(default=False, db_index=True)
    is_background_check = models.NullBooleanField(default=False, db_index=True)

    
class PoliceProfile(models.Model):
    #using the custom User model for authentication. the MyUser class has a OneToOne relationsip which creates a user profile for each user
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    police_id = models.CharField( max_length=50, blank=True, null=True)
    phone_number = models.CharField( max_length=50, blank=True, null=True)
    nationality = models.CharField( max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    profile_pic = models.ImageField( upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    







    