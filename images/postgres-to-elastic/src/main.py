from psycopg2.extensions import connection

from db.postgres import get_postgres


def postgres_to_elastic(postgres: connection):
    pass


if __name__ == '__main__':
    with get_postgres() as postgres_connection:
        postgres_to_elastic(postgres_connection)
