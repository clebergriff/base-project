
import uuid
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import UserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import base64
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile


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
    objects = UserManager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    thumbnail = models.CharField(max_length=2048, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ImageModel(models.Model):

    def upload_location(self, filename):
        return 'images/%s' % (filename)

    image = models.ImageField(upload_to=upload_location, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.image.name

    @classmethod
    def create_from_base64(self, base64_string):
        format, imgstr = base64_string.split(';base64,')
        ext = format.split('/')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        data = ContentFile(base64.b64decode(imgstr), name=filename)
        new_image = self(image=data)
        new_image.save(filename)
        return new_image

    @ property
    def url(self):
        return self.image.url

    def save(self, *args, **kwargs):
        super(ImageModel, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.save(self.image.path)

# when saving a new image, if the image.
