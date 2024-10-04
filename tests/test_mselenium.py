from unittest import TestCase

from m_pyutil.mselenium import ChromeCli


class TestChromeCli(TestCase):

    def test_get(self):
        chrome_cli = ChromeCli()
        chrome_cli.get('https://www.baidu.com')
