import unittest
from unittest.mock import MagicMock, patch
from mongo_client import get_user_by_username, insert_user
from argon2 import PasswordHasher
from dotenv import load_dotenv
import jwt
import os

load_dotenv()
JWTsecret = os.getenv('JWTsecret') # JWT secret key

ph = PasswordHasher() # Argon 2 hashing object

# Import the functions you want to test
from auth import generateToken, getUserFromToken, hashPassword, determineHashMatch, accountCreate, accountLogin, authConnect

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.email = "test@example.com"
        self.role = "user"
        self.token = "testtoken"

    # Test for generateToken function
    def test_generateToken(self):
        token = generateToken(self.username)
        self.assertIsInstance(token, str)

    # Test for getUserFromToken function
    def test_getUserFromToken(self):
        token = jwt.encode({"user": self.username.lower()}, JWTsecret, algorithm="HS256")
        result, user = getUserFromToken(token)
        self.assertTrue(result)
        self.assertEqual(user, self.username.lower())

    # Test for hashPassword function
    def test_hashPassword(self):
        hashed_password = hashPassword(self.password)
        self.assertIsInstance(hashed_password, str)

    # Test for determineHashMatch function
    def test_determineHashMatch(self):
        stored_pass_hash = ph.hash(self.password)
        self.assertTrue(determineHashMatch(stored_pass_hash, self.password))

    # Test for accountCreate function
    @patch('auth.get_user_by_username', return_value=None)
    @patch('auth.insert_user', return_value=None)
    def test_accountCreate(self, mock_insert_user, mock_get_user_by_username):
        success, token = accountCreate(self.username, self.password, self.email, self.role)
        self.assertTrue(success)
        self.assertIsInstance(token, str)

    # Test for accountLogin function
    @patch('auth.get_user_by_username', return_value={"Pwd": ph.hash("testpassword")})
    def test_accountLogin(self, mock_get_user_by_username):
        success, token = accountLogin(self.username, self.password)
        self.assertTrue(success)
        self.assertIsInstance(token, str)

    # Test for authConnect function
    def test_authConnect(self):
        result = authConnect(self.token)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()