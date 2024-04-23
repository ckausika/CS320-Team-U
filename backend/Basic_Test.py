#Create test using pyunit

import unittest

class TestAuth(unittest.TestCase):
    def test_generateToken(self):
        # Test the generateToken function
        self.assertEqual(generateToken("test"), "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCJ9.1GZ6QmW7QrZy7qZL3KoVYQ")
        #check if it returns a string
        self.assertIsInstance(generateToken("test"), str)
    def test_getUserFromToken(self):
        # Test the getUserFromToken function
        self.assertEqual(getUser(FromToken("test"), (True, "test"))

    def test_hashPassword(self):
        # Test the hashPassword function
        self.assertEqual(hashPassword("test"), "$argon2id$v=19$m=102400,t=2,p=8$V2FyZ2FuZw$1GZ6QmW7QrZy7qZL3KoVYQ")

    def test_determineHashMatch(self):
        # Test the determineHashMatch function
        self.assertTrue(determineHashMatch("$argon2id$v=19$m=102400,t=2,p=8$V2FyZ2FuZw$1GZ6QmW7QrZy7qZL3KoVYQ", "test"))

    def test_accountCreate(self):
        # Test the accountCreate function
        self.assertTrue(accountCreate("test", "test", "test", "test"))
    def test_accountLogin(self):
        # Test the accountLogin function
        self.assertTrue(accountLogin("test", "test"))
        self.assertFalse(accountLogin("test", "test2"))

if __name__ == '__main__':

    unittest.main()

                         

