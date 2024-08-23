import unittest
from unittest.mock import patch
from login_logic import check_credentials, register_account
import data


class TestLoginLogic(unittest.TestCase):
    def setUp(self):
        data.users = {}

    def test_incorrect_user_and_password(self):
        self.assertFalse(check_credentials('helo', 'password'))

    def test_correct_user_and_incorrect_password(self):
        self.assertFalse(check_credentials('user', 'password'))

    def test_incorrect_user_and_correct_password(self):
        self.assertFalse(check_credentials('helo', 'pass'))

    def test_correct_user_and_correct_password(self):
        self.assertTrue(check_credentials('stephen', 'password123'))

    def test_register_successful(self):
        result = register_account('New Member', 'New Pass', 'New Pass')
        self.assertEqual(result, "Registration successful!")

    def test_register_username_exists(self):
        with patch('data.get_user', return_value={'New User': 'DoesExist'}):
            result = register_account('New User', 'New Pass', 'New Pass')
        self.assertEqual(result, "Username already exists. Please choose a different one.")

    def test_register_password_mismatch(self):
        result = register_account('new_user', 'password123', 'password456')
        self.assertEqual(result, "Passwords do not match. Please try again.")


if __name__ == "__main__":
    unittest.main()
