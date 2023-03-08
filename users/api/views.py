from django.contrib.auth import get_user_model

from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from pets.models import PetDog

from users.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=("post",))
    def add_pet(self, request, pk=None):
        user = self.get_object()
        pet_id = request.data.get("pet_id")
        pet = PetDog.objects.get(pk=pet_id)
        pet.owners.add(user)
        return response.Response(
            {"message": "pet added"}, status=status.HTTP_201_CREATED
        )
