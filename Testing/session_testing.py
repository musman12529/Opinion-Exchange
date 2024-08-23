import unittest
from unittest.mock import patch
from server import app


class ServerTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_session(self):
        with app.test_client() as client:
            with patch('login_logic.check_credentials', return_value=True):
                client.post('/login', data={'username': 'test_user', 'password': 'test_password'})
                response = client.get('/home')
                self.assertIn(b'Session created', response.data)

    def test_check_multiple_sessions(self):
        with app.test_client() as client:
            with patch('login_logic.check_credentials', return_value=True):
                client.post('/login', data={'username': 'user1', 'password': 'pass1'})
                response1 = client.get('/home')
                self.assertIn(b'Session created', response1.data)
            with patch('login_logic.check_credentials', return_value=True):
                client.post('/login', data={'username': 'user2', 'password': 'pass2'})
                response2 = client.get('/home')
                self.assertIn(b'Session created', response2.data)
            self.assertNotEqual(response1.data, response2.data)

    def test_session_timeout_handler(self):
        with app.test_client() as client:
            with patch('login_logic.check_credentials', return_value=True):
                client.post('/login', data={'username': 'test_user', 'password': 'test_password'})
                response = client.get('/home')
                self.assertIn(b'Session created', response.data)
            import time
            time.sleep(4)
            response_after_timeout = client.get('/home')
            self.assertIn(b'Redirecting', response_after_timeout.data)


if __name__ == '__main__':
    unittest.main()
