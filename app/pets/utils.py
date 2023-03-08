import requests

from http import HTTPStatus

from django.conf import settings
from rest_framework import exceptions


def get_dog_breeds() -> list[str] | None:
    """ This function retrieves a list of dog breeds from dog.ceo's Free API
    :return: A list of dog breeds
    """
    url: str = settings.EXTERNAL_URLS['DOG_BREEDS_URL']
    r = requests.get(url)
    if r.status_code != HTTPStatus.OK:
        raise exceptions.NotFound(detail='Resource not found')
    data_dog_breeds: dict[str, dict] = r.json()
    return [*data_dog_breeds['message'].keys()]
