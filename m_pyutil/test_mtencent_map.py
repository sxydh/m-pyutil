import os
from unittest import TestCase

from m_pyutil.mtencent_map import TencentMap


class TestTencentMap(TestCase):

    def test_geocoder(self):
        tencent_map = TencentMap(os.environ.get('TENCENT_MAP_KEY'))
        response = tencent_map.geocoder(('104.101589', '30.655520'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 0)
