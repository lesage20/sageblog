from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile', )
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    phone = PhoneField(null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.username = self.user.username
        return super().save(*args, **kwargs)


def save_profile(sender, created, instance, **kwargs):
    # instance.profile.save()
    print(created, instance, sender)
    user = User.objects.get(username=instance)
    Profile.objects.create(user=user)
    print("bonjour")


post_save.connect(save_profile, sender=User)
