from rest_framework import viewsets
from pets.api.serializers import PetSerializer

from pets.models import Pet


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class UserPetsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PetSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Pet.objects.filter(owners=user_id)
