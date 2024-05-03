from os import environ
import logging

import sqlite3
import psycopg2
from psycopg2._psycopg import connection as postgres_connection_object
from psycopg2.extras import DictCursor


class SQLiteDataExtraction:
    def __init__(self, sqlite_connection: sqlite3.Connection):
        self.sqlite_connection = sqlite_connection


class PostgresDataLoader:
    def __init__(self, postgres_connection: sqlite3.Connection):
        self.postgres_connection = postgres_connection


def load_from_sqlite(
        sqlite_connection: sqlite3.Connection,
        postgres_connection: postgres_connection_object
):
    logging.info('Начата выгрузка данных из SQLite и загрузка в PostgreSQL')


if __name__ == '__main__':
    dsn: dict[str, str | int] = {
        'dbname': environ.get('MOVIES_DB_NAME'),
        'user': environ.get('MOVIES_DB_USER'),
        'password': environ.get('MOVIES_DB_PASSWORD'),
        'host': environ.get('MOVIES_DB_HOST'),
        'port': int(environ.get('MOVIES_DB_PORT')),
    }
    with sqlite3.connect('db.sqlite') as sqlite_connection, \
            psycopg2.connect(**dsn, cursor_factory=DictCursor) as postgres_connection:
        load_from_sqlite(
            sqlite_connection=sqlite_connection,
            postgres_connection=postgres_connection,
        )
