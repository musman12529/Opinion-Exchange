#all developer server tests in one
import unittest

from review import ReviewCollection, ReviewItem
import sqlite3
import os
import data

from login_logic import check_credentials, register_account

#SESSION MANAGEMENT IMPORTS
from beaker.middleware import SessionMiddleware
from session_management import simple_app, session_opts  # Import your session management setup




# #DEV1 (Muhammad) EXAMPLE - imports all methods from routes.py (as all of them could be tested)- add other imports if other files needed to be tested
# #from (routes.py) import *

#Clinton unit tests are contained in test_review.py

#Zuhair Tests (Dev3)
class TestMyModuleFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary database for testing
        cls.conn = sqlite3.connect('test_data.db')
        cls.cur = cls.conn.cursor()
        with open('init.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            cls.cur.executescript(sql_script)
            cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Close the database connection and remove the temporary database
        cls.conn.close()
        os.remove('test_data.db')

    def test_createReview(self):
        data.create_user("createReviewUser", "passwordHash")
        data.create_review("Test Topic", "Test Body", 1, False)

        review = data.get_reviews()[-1]
        self.assertEqual(review['topic'], "Test Topic")
        self.assertEqual(review['body'], "Test Body")

    def test_getReviews(self):
        reviews = data.get_reviews()
        self.assertIsInstance(reviews, list)

    def test_updateReview(self):
        data.create_user("updateReviewUser", "passwordHash")
        data.create_review("Test Topic", "Test Body", 1, False)
        review = data.get_reviews()[-1]
        review_id = review['id']
        data.update_review(review_id, "Updated Topic", "Updated Body", 1, True)
        updated_review = data.get_reviews()[-1]
        self.assertEqual(updated_review['topic'], "Updated Topic")
        self.assertEqual(updated_review['body'], "Updated Body")
        self.assertTrue(updated_review['draft'])

    def test_removeReview(self):
        data.create_user("removeReviewUser", "passwordHash")
        data.create_review("Test Topic", "Test Body", 1, False)
        review = data.get_reviews()[-1]
        review_id = review['id']
        data.remove_review(review_id)
        review = data.get_reviews()[-1]
        self.assertNotEqual(review['id'], review_id)

    def test_createComment(self):
        data.create_user("testcreatecommentuser", "passwordhash")
        data.create_review("Test Topic", "Test Body", 1, False)
        review = data.get_reviews()[-1]
        review_id = review['id']
        data.create_comment(review_id, 1, "Test Comment")
        review = data.get_reviews()[-1]
        comments = review['comments']
        self.assertIsInstance(comments, list)
        self.assertEqual(comments[0]['body'], "Test Comment")

    def test_getUser(self):
        data.create_user("testgetuser", "passwordhash")
        user = data.get_user("testgetuser")
        self.assertIsInstance(user, dict)
        self.assertEqual(user['username'], "testgetuser")

    def test_createUser(self):
        data.create_user("testcreateuser", "passwordhash")
        user = data.get_user("testcreateuser")
        self.assertIsInstance(user, dict)
        self.assertEqual(user['username'], "testcreateuser")

    def test_updateUser(self):
        data.create_user("testupdateuser", "passwordhash")
        user = data.get_user("testupdateuser")
        user_id = user['id']
        data.update_user(user_id, "updateduser", "newpasswordhash", "newtoken")
        updated_user = data.get_user("updateduser")
        self.assertEqual(updated_user['username'], "updateduser")
        self.assertEqual(updated_user['passwordHash'], "newpasswordhash")
        self.assertEqual(updated_user['token'], "newtoken")

    def test_removeUser(self):
        data.create_user("testremoveuser", "passwordhash")
        user = data.get_user("testremoveuser")
        user_id = user['id']
        data.remove_user(user_id)
        user = data.get_user("testremoveuser")
        self.assertIsNone(user)


# #DEV4 (Ibrahim) EXAMPLE - imports all methods from data.py (as all of them could be tested)- add other imports if other files needed to be tested
# #from (insert_filename_here) import *


#DEV 5 (Stephen) - Unit testing for login_logic.py - COMPLETE: ALL TEST WORKING PROPERLY

class TestLoginLogic(unittest.TestCase):

    def test_incorrect_user_and_password(self):
        self.assertFalse(check_credentials('helo', 'password'))

    def test_correct_user_and_incorrect_password(self):
        self.assertFalse(check_credentials('user', 'password'))

    def test_incorrect_user_and_correct_password(self):
        self.assertFalse(check_credentials('helo', 'pass'))

    def test_correct_user_and_correct_password(self):
        self.assertTrue(check_credentials('stephen', 'password123'))

class SessionManagementTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a test WSGI application with the session middleware
        self.app = SessionMiddleware(simple_app, session_opts)


    def test_session_id_on_login(self):
        # Simulate a request where a user logs in
        environ = {
            'beaker.session': {},  # Create an empty session
        }
        response_body = self.app(environ, self.dummy_start_response)

        # Check if the session ID is set to 10
        session = environ['beaker.session']
        self.assertIn('user_id', session)
        self.assertEqual(session['user_id'], 10)

        user_cur_id = session['user_id']
        crypto_key_id = session_opts['session.encrypt_key']

        print('\n''\n'''"current user id is:" ,user_cur_id,'\n'"compared to crypto hash key:", crypto_key_id)


    def test_session_security(self):
        # Ensure that the crypto_key is used for session security
        self.assertNotEqual(session_opts['session.encrypt_key'], ['user_id'])

        crypto_key_id = session_opts['session.encrypt_key']
        #print("Hashed Crypto Key:", crypto_key_id)


    def test_multiple_users(self):
        # Simulate requests for multiple users
        users = ['user1', 'user2', 'user3']
        for username in users:
            environ = {
                'beaker.session': {},
            }
            response_body = self.app(environ, self.dummy_start_response)
            session = environ['beaker.session']
            session['user_id'] = username

            # Check if the session ID matches the user's username
            self.assertIn('user_id', session)
            self.assertEqual(session['user_id'], username)
        print('\n''\n'"users logged on:", len(users))
    def dummy_start_response(self, status, headers, exc_info=None):
        pass











if __name__ == "__main__":
    unittest.main()
