from django.contrib.auth import get_user_model
from utils.serializers import BaseModelSerializer


class UserSerializer(BaseModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password",
            "phone_number",
            "city",
            "pets"
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "pets": {"required": False}
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
