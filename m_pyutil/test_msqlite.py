import sqlite3
import uuid
from unittest import TestCase

from m_pyutil.msqlite import get_conn, create, drop, save


class Test(TestCase):
    table_name = 't_test'

    def test_get_conn(self):
        with get_conn() as conn:
            self.assertIsInstance(conn, sqlite3.Connection)

    def test_create(self):
        rowcount = create(sql=f'create table if not exists {self.table_name}(id integer primary key autoincrement, name text)')
        self.assertEqual(rowcount, -1)

    def test_save(self):
        self.test_create()
        rowcount = save(sql=f'insert into {self.table_name}(name) values(?)', params=[str(uuid.uuid4())])
        self.assertEqual(rowcount, 1)

    def test_drop(self):
        self.test_create()
        rowcount = drop(sql=f'drop table {self.table_name}')
        self.assertEqual(rowcount, -1)
