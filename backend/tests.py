import unittest
from unittest.mock import patch, MagicMock
from mongo_client import (
    generateToken,
    getUserFromToken,
    hashPassword,
    determineHashMatch,
    accountCreate,
    accountLogin
)

class TestMongoClient(unittest.TestCase):

    def test_generate_token(self):
        # Test to ensure token generation is successful
        token = generateToken("username", "test@test.com", "role")
        # Assert token is not empty
        self.assertTrue(token)

    def test_get_user_from_token(self):
        # Test to ensure user can be retrieved from a token
        token = generateToken("username", "email@example.com", "role")
        success, user = getUserFromToken(token)
        # Assert successfully decoded token and user is retrieved
        self.assertTrue(success)
        self.assertEqual(user, "username")

    def test_hash_password(self):
        # Test to ensure password hashing is successful
        password = "password"
        hashed_password = hashPassword(password)
        # Assert hashed password is not empty
        self.assertTrue(hashed_password)

    def test_determine_hash_match(self):
        # Test to ensure password hash verification is successful
        stored_hash = hashPassword("password")
        input_password = "password"
        # Assert password matches stored hash
        self.assertTrue(determineHashMatch(stored_hash, input_password))
'''
    @patch('mongo_client.get_user_by_username')
    @patch('mongo_client.insert_user')
    def test_account_create(self, mock_insert_user, mock_get_user_by_username):
        # Test to ensure account creation is successful
        mock_get_user_by_username.return_value = []
        success, _ = accountCreate("username", "password", "email@example.com", "Student")
        # Assert account creation is successful
        self.assertTrue(success)
        # Assert insert_user was called with correct arguments
        mock_insert_user.assert_called_once()

    @patch('mongo_client.get_user_by_username')
    def test_account_login(self, mock_get_user_by_username):
        # Test to ensure account login is successful
        mock_get_user_by_username.return_value = [{"Pwd": hashPassword("password"), "Email": "email@example.com", "Role": "Student"}]
        success, _ = accountLogin("username", "password")
        # Assert login is successful
        self.assertTrue(success)
'''
if __name__ == '__main__':
    unittest.main()
