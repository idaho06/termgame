import unittest
import importlib
from res import config

config.database_file = "test.sqlite"
import os


class TestSession(unittest.TestCase):
    def setUp(self):
        try:
            os.remove(config.database_file)
        except:
            print("setUp: Database %s already deleted" % config.database_file)

    def tearDown(self):
        try:
            os.remove(config.database_file)
        except:
            print("tearDown: Database %s already deleted" % config.database_file)

    def test_session(self):
        from res import session
        self.assertEqual(1, session.__session__)
        self.assertEqual(False, session.is_ddbb_open)
