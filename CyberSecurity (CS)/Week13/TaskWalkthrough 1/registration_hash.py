import hashlib
import os


def hash_password(password):
    # Generate random salt
    salt = os.urandom(16)

    # Encode password
    password = password.encode()

    # Parse the password + salt into the hashing algorithm.
    hashed = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)

    # Write the salt and Full Hash to the salts.txt file.
    with open('salts.txt', 'a') as file:
        file.write(f"salt: {salt}\nFull Hash: {hashed.hex()}")

    # Return the salt and full hash
    return salt + hashed


print(hash_password("VerySecurePassword9000!"))
