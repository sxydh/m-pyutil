import os
from unittest import TestCase

from m_pyutil.mjuliangip import DynamicIP


class Test(TestCase):

    def test_dynamic_get_ips(self):
        ju_liang_ip = DynamicIP(os.environ.get('JULIANGIP_API_KEY'))
        ips = ju_liang_ip.get_ips(trade_no=os.environ.get('JULIANGIP_TRADE_NO'))
        print(ips)
