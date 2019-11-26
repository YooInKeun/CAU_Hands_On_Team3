from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=20, blank=True, default="")
    nickname = models.CharField(max_length=10, blank=True, default="")
    image = models.ImageField(blank=True)
    student_number = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=10, blank=True, default="")

    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()