from os import environ

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FASTAPI_HOST: str = environ.get('FASTAPI_HOST')
    FASTAPI_PORT: int = int(environ.get('FASTAPI_PORT'))

    REDIS_HOST: str = environ.get('REDIS_HOST')
    REDIS_PORT: int = int(environ.get('REDIS_PORT'))

    ELASTIC_HOST: str = environ.get('ELASTIC_HOST')
    ELASTIC_PORT: int = int(environ.get('ELASTIC_PORT'))


settings = Settings()