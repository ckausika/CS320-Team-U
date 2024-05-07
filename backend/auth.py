from mongo_client import get_user_by_username, insert_user
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

# Generate a JWT token based off the username and the JWT secret
def generateToken(user, email, role):
    encoded_jwt = jwt.encode({"user": user, "email": email, "role": role}, JWTsecret, algorithm="HS256")

    return encoded_jwt;

def getUserFromToken(token):
    try:
        decoded_jwt = jwt.decode(token, JWTsecret, algorithms=["HS256"])


        return True, decoded_jwt["user"]
    except jwt.InvalidSignatureError: # The secret is wrong!
        return False, "-1"

# Hashes the pasword with Argon2 and returns the hash
def hashPassword(plainTextPassword):
    return ph.hash(plainTextPassword)

# Returns boolean if the input pass matches the stored hash
def determineHashMatch(storedPassHash, inputPass):
    try:
        ph.verify(storedPassHash, inputPass)
        return True
    except:
        return False

# Create an account given a username and password
def accountCreate(username, password, email, role):
    # Determine if the account with the specified username already exists in the DB
    loweredName = username.lower()

    foundAccount = get_user_by_username(loweredName)
    if len(foundAccount) == 0:
        # The account does not exist in the DB!

        # If the person isn't a professor then default them to being a Student
        if role != "Professor":
            role = "Student"

        # Insert a new user in the database
        insert_user(email, loweredName, hashPassword(password), role) # CHECK IF FAILURE???
        # Return a success response and the token
        return True, generateToken(username, email, role)
    else:
        return False, "Already exists!"


# Login to an account given a username and password
def accountLogin(username, password):
    loweredName = username.lower()
    foundAccount = get_user_by_username(loweredName)

    # Account with specified username does not exist in the DB
    if foundAccount is None:
        return False, "INVALID"

    if(determineHashMatch(foundAccount[0]["Pwd"], password)):
        # If the two passwords match then generate a token and send to the user!
        return True, generateToken(username, foundAccount[0]["Email"], foundAccount[0]["Role"])
    else:
        # If the password is not correct then return false!
        return False, "INVALID"