from dns.dns import (get_flags)
from .base_test import BaseTest


class TestDNS(BaseTest):
    def test_get_flags(self):
        mock_data = int(1).to_bytes(1, byteorder='big') * 2
        self.assertEqual(get_flags(mock_data), b'\x84\x00')
