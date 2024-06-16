import os
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

class PostgreConnector:
    def __init__(self):
        self.connection_params = {
            'host': os.getenv("DB_HOST"),
            'database': os.getenv("DB_NAME"),
            'user': os.getenv("DB_USER"),
            'password': os.getenv("DB_PASSWORD"),
            'port': os.getenv("DB_PORT")
        }

    def _get_connection(self):
        return psycopg2.connect(**self.connection_params)

    def execute_query(self, query, params=None):
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()

    def fetch_query(self, query, params=None):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

    def fetch_query_one(self, query, params=None):
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
