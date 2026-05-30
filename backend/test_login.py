import unittest
from app import create_app

class AdminLoginTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app(testing=True)
        self.client = self.app.test_client()

    def test_login_invalid_credentials(self):
        response = self.client.post('/api/admin/login', json={
            'email': 'wrong@example.com',
            'password': 'invalid'
        })
        self.assertEqual(response.status_code, 401)

    def test_login_missing_fields(self):
        response = self.client.post('/api/admin/login', json={})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
