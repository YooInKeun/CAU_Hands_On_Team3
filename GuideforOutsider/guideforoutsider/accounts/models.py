from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=20, blank=True, default="")
    nickname = models.CharField(max_length=10, blank=True, default="")
    phone = models.CharField(max_length=15, blank=True, default="")
    zip_code = models.CharField(max_length=10, blank=True, default="")
    address = models.CharField(max_length=20, blank=True, default="")
    address_detail = models.CharField(max_length=10, blank=True, default="")
    image = models.ImageField(blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()