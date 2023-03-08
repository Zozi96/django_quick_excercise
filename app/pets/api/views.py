from rest_framework import viewsets, response
from rest_framework.decorators import action

from pets.models import PetDog
from pets.utils import get_dog_breeds
from pets.api.serializers import PetDogSerializer, DogBreedSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = PetDog.objects.all()
    serializer_class = PetDogSerializer

    @action(methods=('get',), detail=False, url_path='list-breeds', url_name='list_breeds')
    def list_breeds(self, request):
        serializer = DogBreedSerializer({'list_breeds': get_dog_breeds()})
        return response.Response(data=serializer.data)
