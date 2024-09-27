from urllib.parse import quote

import requests


class TencentMap:

    def __init__(self, key: str):
        self.key = quote(key or '')

    def geocoder(self, location: tuple):
        lng = quote(location[0])
        lat = quote(location[1])
        return requests.get(f'https://apis.map.qq.com/ws/geocoder/v1?location={lat},{lng}&key={self.key}')
