from http import HTTPStatus
import requests
from rest_framework import exceptions


def get_dog_breeds() -> list[str] | None:
    url: str = 'https://dog.ceo/api/breeds/list/all'  # It's a free api to retrieve dog breeds
    r = requests.get(url)
    if r.status_code != HTTPStatus.OK:
        raise exceptions.NotFound(detail='Resource not found')
    data_dog_breeds: dict[str, dict] = r.json()
    return [*data_dog_breeds['message'].keys()]
