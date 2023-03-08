from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class GenderChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"


class PetDog(models.Model):
    birth_date = models.DateField(verbose_name='Birth date')
    gender = models.CharField(verbose_name='Gender', max_length=1, choices=GenderChoices.choices)
    weight = models.FloatField(verbose_name='Weight')
    breed = models.CharField(verbose_name='Breed', max_length=100)
    deceased_date = models.DateField(verbose_name='Deceased date', null=True, blank=True)
    owners = models.ManyToManyField(to=get_user_model(), related_name='pets')

    @property
    def age(self):
        today = now().today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self) -> str:
        return f'Gender: {self.gender} Weight: {self.weight} Breed: {self.breed}'
