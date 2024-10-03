from unittest import TestCase

from m_pyutil.mip import get_ip


class Test(TestCase):

    def test_get_ip(self):
        ip = get_ip()
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        self.assertRegex(ip, regexp)
