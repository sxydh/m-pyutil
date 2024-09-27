import logging
import os
import sqlite3
from sqlite3 import Connection

DEFAULT_DB_FILE = 'sqlite.db'


def get_conn(f: str = DEFAULT_DB_FILE) -> Connection:
    os.makedirs('tmp', exist_ok=True)
    return sqlite3.connect(f'tmp/{f}')


def save(sql: str, params: list = None, f: str = DEFAULT_DB_FILE) -> int:
    while True:
        with get_conn(f) as conn:
            # noinspection PyBroadException
            try:
                cur = conn.execute(sql, params)
                conn.commit()
                return cur.rowcount
            except Exception as e:
                if 'database is locked' in str(e):
                    continue
                logging.warning(e)
                return 0
