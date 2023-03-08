from rest_framework import serializers
from utils.serializers import BaseSerializer, BaseModelSerializer

from pets.models import PetDog


class DogBreedSerializer(BaseSerializer):
    list_breeds = serializers.ListField(read_only=True, child=serializers.CharField())


class PetDogSerializer(BaseModelSerializer):
    age = serializers.ReadOnlyField()

    class Meta:
        model = PetDog
        exclude = ('owners',)
