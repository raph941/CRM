from django.db.models.signals import post_save
from .models import Criminal
from django.dispatch import receiver
from .models import CriminalImage

@receiver(post_save, sender=Criminal)
def Create_criminalimage(sender, instance, created, **kwargs):
    if created:
        CriminalImage.objects.create(criminal=instance)

@receiver(post_save, sender=Criminal)
def save_criminalimage(sender, instance, **kwargs):
    instance.criminalimage.save()