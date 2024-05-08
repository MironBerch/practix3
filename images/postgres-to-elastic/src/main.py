from elasticsearch import Elasticsearch
from psycopg2.extensions import connection
from redis import Redis

from db.elastic import get_elastic
from db.postgres import get_postgres
from db.redis import get_redis


def postgres_to_elastic(
        postgres: connection,
        elastic: Elasticsearch,
        redis: Redis,
):
    pass


if __name__ == '__main__':
    with get_postgres() as postgres_connection:
        with get_elastic() as elastic_connection:
            with get_redis() as redis_connection:
                postgres_to_elastic(
                    postgres=postgres_connection,
                    elastic=elastic_connection,
                    redis=redis_connection,
                )
