import os
from unittest import TestCase

from m_pyutil.mjuliangip import DynamicIP


class Test(TestCase):

    def test_dynamic_get_ips(self):
        ju_liang_ip = DynamicIP(os.environ.get('JULIANGIP_API_KEY'))
        response = ju_liang_ip.dynamic_get_ips(trade_no=os.environ.get('JULIANGIP_TRADE_NO'))
        self.assertEqual(response.status_code, 200)
        print(response.json())
