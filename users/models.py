from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from utils.picture import delete_profile_picture


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r"^\+?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(verbose_name="Phone Number", validators=(phone_regex,), max_length=17, blank=True)
    city = models.CharField(verbose_name="City", max_length=100, blank=True)
    last_login = models.DateTimeField(verbose_name="Last login", auto_now=True)
    email = models.EmailField(verbose_name="Email address", unique=True)
    profile_picture = models.FileField(verbose_name='Profile picture', upload_to='users-profile-pictures', null=True)


@receiver(pre_save, sender=User)
def delete_previous_image(sender, instance, **kwargs) -> None:
    delete_profile_picture(sender, instance)
