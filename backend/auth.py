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

import argon2 from PasswordHasher

ph = passwordHasher() # Argon 2 hashing object

# FUNCTION: determineHashMatch
# Given a username, input, and data type, search for a hash
# in the database and compare the two to see if they match.
#
# Input: (user: 'Username', unhashedInput: 'Unhashed password input', Type: 'Password'/'Token')
# Output: Boolean (Success/Failure)
#

def determineHashMatch(user, unhashedInput, type)
    if type == 'Password':
        # Get stored password hash of user from the DB
        #storedPasswordHash = ?

        # Compare unhashed target to the stored password
        #return ph.verify(storedPasswordHash, target)
    elif type == 'Token':
        # Get stored token hash of user from the DB
        #storedTokenHash = ?

        # Compare unhashed target to the stored token
        #return ph.verify(storedTokenHash, target)
    else:
        return False # An unknown type was given to the function

# Create an account given a username and password
def accountCreate(username, password):
    # Check if account with that username already exists
    return false

# Login to an account given a username and password
def accountLogin(username, password):
    return false

# Perform an authentication request given a token
def authConnect(token):
    return false