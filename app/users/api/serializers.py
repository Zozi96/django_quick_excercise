from django.contrib.auth import get_user_model

from pets.api.serializers import PetDogSerializer
from utils.serializers import BaseModelSerializer


class UserCreationSerializer(BaseModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'pk',
            'username',
            'email',
            'password',
            'phone_number',
            'city',
        )
        read_only_fields = ('pk',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'city',
            'profile_picture'
        )


class UserAddPetSerializer(BaseModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pets',)


class UserPetSerializer(BaseModelSerializer):
    pets = PetDogSerializer(read_only=True, many=True, context={'excluded_fields': ['id']})

    class Meta:
        model = get_user_model()
        fields = ('pets',)
