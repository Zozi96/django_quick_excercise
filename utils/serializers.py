from typing import Iterable

from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs) -> None:
        context = kwargs.get('context', {})
        excluded_fields: Iterable = context.get('excluded_fields', [])

        if excluded_fields:
            for field in excluded_fields:
                self.fields.pop(field, None)

        super().__init__(*args, **kwargs)


class BaseModelSerializer(BaseSerializer, serializers.ModelSerializer):
    pass
