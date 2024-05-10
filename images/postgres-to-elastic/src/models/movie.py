from typing import Any, ClassVar

from models.base import UUIDMixin
from models.person import Person


class Movie(UUIDMixin):
    """Класс для валидации данных `filmwork`."""

    rating: float = 0.0
    genre: list[str]
    title: str
    description: str
    actors_names: list[str] = []
    writers_names: list[str] = []
    directors_names: list[str] = []
    actors: list[Person] = []
    writers: list[Person] = []
    directors: list[Person] = []
    _index: ClassVar[str] = 'movies'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.rating is None:
            self.rating = 0.0

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
