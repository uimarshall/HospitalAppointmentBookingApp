from flask_testing import TestCase
from app import app
import unittest

# python -m unittest test_app


class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        assert b'container' in rv.data
        #assert False

    def test_add(self):
        rv = self.app.get('/about')
        self.assertEqual(rv.status, '200 OK')

        rv = self.app.get('/bookingdetails')
        self.assertEqual(rv.status, '200 OK')

    def test_404(self):
        rv = self.app.get('/other')
        self.assertEqual(rv.status, '404 NOT FOUND')


if __name__ == '__main__':
    unittest.main()
