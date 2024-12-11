import hashlib

# Original salt to be added to password provided by the user to try and regenerate the FULL HASH Below
SALTED = b'B\x8fjj\x14\xd1\xc4<\xbb\x99\x89m\xaf\x0f\x8e{'
FULLHASH = '''296cc27c692604b4fa7cc7cde66602ff558d8f70b66460922a891c890d5cfea6'''


def hash_password(password):
    # Encode password
    password = password.encode()

    # Parse the password + salt into the hashing algorithm.
    hashed = hashlib.pbkdf2_hmac('sha256', password, SALTED, 100000)

    # Return the salt and full hash
    return "Logged in!" if hashed.hex() == FULLHASH else "Authentication failed!"


password = input("Enter your password: ")
print(hash_password(password))
