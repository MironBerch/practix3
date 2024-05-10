from typing import Any, ClassVar

from models.base import UUIDMixin
from models.person import Person


class Movie(UUIDMixin):
    """Класс для валидации данных `filmwork`."""

    rating: float
    genre: list[str]
    title: str
    description: str
    director: list[str]
    actors_names: list[str]
    writers_names: list[str]
    actors: list[Person]
    writers: list[Person]
    _index: ClassVar[str] = 'movies'

    @classmethod
    def properties(cls, **kwargs) -> dict[str, Any]:
        """Возвращает схему модели фильма с её характеристиками."""
        properties: dict[str, Any] = {}
        for field, value in cls.model_json_schema(**kwargs)['properties'].items():
            if value['type'] == 'string':
                properties[field] = ''
            if value['type'] == 'array':
                properties[field] = []
            if value['type'] == 'number':
                properties[field] = 0
        return properties
