from app import app

import os
import unittest

class AppTestCase(unittest.TestCase):

   def test_root_text(self):
        tester = app.test_client(self)
        response = tester.get('/')
        # Fix: unit tests failed because of the type error
        # assert 'Hello world!' in response.data
        assert b'Hello world!' in response.data

if __name__ == '__main__':
    unittest.main()
