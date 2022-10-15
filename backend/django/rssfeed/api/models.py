
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import UserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=2048)
    thumbnail = models.URLField(max_length=2048, blank=True)
    published_date = models.DateTimeField()
    language = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    objects = UserManager()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
