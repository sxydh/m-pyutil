import socket

import psutil


def get_ip(nic_name: str = 'WLAN'):
    for name, addresses in psutil.net_if_addrs().items():
        if name == nic_name:
            for address in addresses:
                if address.family == socket.AF_INET:
                    return address.address
