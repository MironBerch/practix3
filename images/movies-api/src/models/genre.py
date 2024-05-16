from models.base import UUIDMixin


class BaseGenre(UUIDMixin):
    """Базовая модель жанра."""

    name: str

    class Config:
        allow_population_by_field_name = True


class Genre(BaseGenre):
    """Модель жанра."""

    description: str
