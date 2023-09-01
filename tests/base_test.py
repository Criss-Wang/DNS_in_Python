import io
import logging
import sys
from unittest import TestCase


class BaseTest(TestCase):
    def setUp(self):
        logging.info("=" * 60)
        logging.info(f"{self.id()} start")
        self.stdout = io.StringIO()
        self.stdout_backup, sys.stdout = sys.stdout, self.stdout
