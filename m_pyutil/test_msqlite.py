import sqlite3
from unittest import TestCase

from m_pyutil.msqlite import get_conn


class Test(TestCase):

    def test_get_conn(self):
        conn = get_conn()
        self.assertIsInstance(conn, sqlite3.Connection)
