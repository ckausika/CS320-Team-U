# Todo:
# 1. Connect to auth API endpoints
#
# 2. Find a hashing function we can import
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
# Required stored data for each account's authentication
# [USERNAME, HASHED PASSWORD, HASHED TOKEN]