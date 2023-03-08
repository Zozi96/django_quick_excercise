from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from django.db import models


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r"^\+?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(verbose_name="Phone Number", validators=(phone_regex,), max_length=17)
    city = models.CharField(verbose_name="City", max_length=100)
    last_login = models.DateTimeField(verbose_name="Last login", auto_now=True)
    email = models.EmailField(verbose_name="Email address", unique=True)
    profile_picture = models.FileField(verbose_name='Profile picture', upload_to='users-profile-pictures', null=True)



