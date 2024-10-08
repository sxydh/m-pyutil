import sqlite3
import uuid

from m_pyutil.msqlite import get_conn, create, drop, save, select, select_one, selectd, selectd_one
from tests._TestCase import _TestCase


class Test(_TestCase):
    table_name = 't_test'

    def test_get_conn(self):
        with get_conn() as conn:
            self.assertIsInstance(conn, sqlite3.Connection)

    def test_create(self):
        rowcount = create(sql=f'create table if not exists {self.table_name}(id integer primary key autoincrement, name text)')
        self.assertEqual(rowcount, -1)

    def test_drop(self):
        self.test_create()
        rowcount = drop(sql=f'drop table {self.table_name}')
        self.assertEqual(rowcount, -1)

    def test_save(self):
        self.test_create()
        rowcount = save(sql=f'insert into {self.table_name}(name) values(?)', params=[str(uuid.uuid4())])
        self.assertEqual(rowcount, 1)

    def test_select(self):
        self.test_save()
        rows = select(sql=f'select * from {self.table_name}')
        self.assertIs(len(rows) > 0, True)

    def test_selectd(self):
        self.test_save()
        rows = selectd(sql=f'select * from {self.table_name}')
        self.assertIs(len(rows) > 0, True)

    def test_select_one(self):
        self.test_save()
        row = select_one(sql=f'select * from {self.table_name}')
        self.assertEqual(row[0], 1)

    def test_selectd_one(self):
        self.test_save()
        row = selectd_one(sql=f'select * from {self.table_name}')
        self.assertEqual(row.get('id'), 1)
