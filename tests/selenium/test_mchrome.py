from unittest import TestCase

from m_pyutil.selenium.mchrome import ChromeCli


class TestChromeCli(TestCase):

    def test_get(self):
        chrome_cli = ChromeCli()
        chrome_cli.get('https://www.baidu.com')
        nav = chrome_cli.query_element_d('id', 's-top-left')
        nav_text = nav.text
        self.assertIsInstance(nav_text, str)
