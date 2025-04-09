import psycopg2
from psycopg2 import DatabaseError
from decouple import  config as decouple_config


def get_connection():
    try:
        return psycopg2.connect(
            host=decouple_config('PGSQL_HOST'),
            user=decouple_config('PGSQL_USER'),
            password=decouple_config('PGSQL_PASSWORD'),
            database=decouple_config('PGSQL_DATABASE')
        )
    except ValueError as ex:
        raise ex