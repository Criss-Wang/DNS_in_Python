from dns import dns
from .base_test import BaseTest

import os
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)
path = os.path.abspath(dns.__file__)

class TestDNS(BaseTest):
    def test_get_flags(self):
        logging.info(path)
        mock_data = int(1).to_bytes(1, byteorder='big') * 2
        self.assertEqual(dns.get_flags(mock_data), b'\x84\x00')
