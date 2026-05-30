import unittest
from backend.app import create_app

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(testing=True)
        self.client = self.app.test_client()

    def test_admin_login_invalid(self):
        response = self.client.post('/api/admin/login', json={
            'email': 'wrong@example.com',
            'password': 'nope'
        })
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
