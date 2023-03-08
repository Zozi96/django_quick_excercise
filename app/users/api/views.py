from django.contrib.auth import get_user_model
from rest_framework import viewsets, response, permissions
from rest_framework.decorators import action
from rest_framework.request import Request

from users.api.serializers import UserCreationSerializer, UserUpdateSerializer, UserAddPetSerializer, UserPetSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreationSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            self.permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            self.serializer_class = UserUpdateSerializer
        elif self.action == 'my_pets':
            if self.request.method == 'PUT':
                self.serializer_class = UserAddPetSerializer
            elif self.request.method == 'GET':
                self.serializer_class = UserPetSerializer
        return super().get_serializer_class()

    @action(methods=('put', 'get'), detail=True, url_path='my-pets', url_name='my_pets')
    def my_pets(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return response.Response(serializer.data)
