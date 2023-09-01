from dns.dns import get_flags

from .base_test import BaseTest

class TestDNS(BaseTest):
    def test_get_flags(self):
        mock_data = b'\x00\x01'
        self.assertEqual(get_flags(mock_data), b'\x00\x01')
        