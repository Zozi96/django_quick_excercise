from rest_framework import viewsets
from pets.api.serializers import PetSerializer

from pets.models import Pet


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
