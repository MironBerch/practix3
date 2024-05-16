from fastapi import APIRouter

from src.api.v1.handlers import genres, health, movies, persons

api_v1_router = APIRouter(prefix='/v1')

# Healthcheck
api_v1_router.include_router(router=health.router, prefix='/healthcheck')

# Movies
api_v1_router.include_router(router=movies.router, prefix='/healthcheck')

# Genres
api_v1_router.include_router(router=genres.router, prefix='/healthcheck')

# Persons
api_v1_router.include_router(router=persons.router, prefix='/healthcheck')
