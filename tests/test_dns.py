from dns import dns
from .base_test import BaseTest


class TestDNS(BaseTest):
    def test_get_flags(self):
        mock_data = int(1).to_bytes(1, byteorder='big') * 2
        self.assertEqual(dns.get_flags(mock_data), b'\x84\x00')
