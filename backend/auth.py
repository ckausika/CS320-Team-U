# Todo:
# 1. Connect to auth API endpoints
#
# 2. Find a hashing function we can import https://pypi.org/project/argon2-cffi/
#
# 3. Create authentication token generation function. Have DB store a
#    hashed version of that token so they are securely stored and
#    not in plain-text.
#
# 4. Create account creation function. Ensure the same username does not already
#    exist in the DB. Then hash password and store it in the DB with the plain-text
#    username. Create (refer to todo #3) and return the unhashed token to the client
#    so they can store it as a cookie.
#
# 5. Create login function. Hash password input and compare it, and the username,
#    to the ones stored in the DB. If both good match, then replace current token
#    with a new one (refer to todo #3 for token creation) and return the unhashed
#    token to the client so they can store it as a cookie.
#
# 6. For requests requiring authentication, receive token from client. Hash the token
#    and compare it to hashed version in the DB. If good match, go ahead with whatever
#    data retrieval that is requested.
#
# 7. Create logout function. Receive token from the client and hash it and then
#    compare it to the one stored in the database. If match, erase that client's
#    stored, hashed token from the DB so it can not be used to log in again.
#
# Required stored data for each account's authentication
# [USERNAME, HASHED PASSWORD, HASHED TOKEN]

from argon2 import PasswordHasher
from dotenv import load_dotenv
import jwt
import os

load_dotenv()
JWTsecret = os.getenv('JWTsecret') # JWT secret key

ph = PasswordHasher() # Argon 2 hashing object

# FUNCTION: determineHashMatch
# Given a username, input, and data type, search for a hash
# in the database and compare the two to see if they match.
#
# Input: (user: 'Username', unhashedInput: 'Unhashed password input', Type: 'Password'/'Token')
# Output: Boolean (Success/Failure)
#

def generateToken(user):
    encoded_jwt = jwt.encode({"user": user}, JWTsecret, algorithm="HS256")

    return encoded_jwt;

def getUserFromToken(token):
    try:
        decoded_jwt = jwt.decode(token, JWTsecret, algorithms=["HS256"])


        return True, decoded_jwt["user"]
    except jwt.InvalidSignatureError: # The secret is wrong!
        return False, "-1"

#print(verifyUserByToken(generateToken("abc")))

def determineHashMatch(user, unhashedInput):
    #if type == 'Password':
        # Get stored password hash of user from the DB
        #storedPasswordHash = ?

        # Compare unhashed target to the stored password
        #return ph.verify(storedPasswordHash, target)
    #elif type == 'Token':
        # Get stored token hash of user from the DB
        #storedTokenHash = ?

        # Compare unhashed target to the stored token
        #return ph.verify(storedTokenHash, target)
    #else:
    return True # An unknown type was given to the function

# Create an account given a username and password
def accountCreate(username, password):
    # If username in DB already exists then return False

    
    print("acc create ran")
    return False

# Login to an account given a username and password
def accountLogin(username, password):
    # return "INVALID"
    # compare username & password in db. if good then return token:

    #def get_user_by_username(username: str) -> dict:
    #users_collection = mydb["user_information"]
    #return users_collection.find_one({"Username":username})
    foundAccount = get_user_by_username(username)

    if(determineHashMatch(password, foundAccount["password"])):
        # If the two passwords match then generate a token and send to the user!
        return generateToken(username)
    else:
        # If the password is not correct then return false!
        return False;

    #return verifyUserByToken(generateToken(username))

# Perform an authentication request given a token
def authConnect(token):
    return False