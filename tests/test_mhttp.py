from socketserver import TCPServer
from unittest import TestCase

from m_pyutil.mhttp import Server


class Test(TestCase):

    def test_server(self):
        server = Server().start()
        self.assertIsInstance(server, TCPServer)
        server.close()
