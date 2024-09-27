import sqlite3
from unittest import TestCase

from m_pyutil.msqlite import get_conn, create


class Test(TestCase):

    def test_get_conn(self):
        with get_conn() as conn:
            self.assertIsInstance(conn, sqlite3.Connection)

    def test_create(self):
        create(sql='create table t_test(id integer primary autoincreamentment)')
