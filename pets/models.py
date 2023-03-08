
from django.db import models
from django.contrib.auth import get_user_model


class Pet(models.Model):
    DOG = "Dog"
    BREED_CHOICES = [
        (DOG, "Dog"),
    ]
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=20, choices=BREED_CHOICES, default=DOG)
    gender = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    deceased_date = models.DateField(null=True, blank=True)
    owners = models.ManyToManyField(get_user_model(), related_name="pets")
