import unittest
from app import app

class TestService2(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertIn('Hello from', data['message'])

if __name__ == '__main__':
    unittest.main()