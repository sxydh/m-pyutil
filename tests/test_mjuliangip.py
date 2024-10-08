import os

from m_pyutil.mjuliangip import DynamicIP
from tests._TestCase import _TestCase


class Test(_TestCase):

    def test_dynamic_get_ips(self):
        dynamic_ip = DynamicIP(os.environ.get('JULIANGIP_API_KEY'))
        ips = dynamic_ip.get_ips(trade_no=os.environ.get('JULIANGIP_TRADE_NO'))
        print(ips)
