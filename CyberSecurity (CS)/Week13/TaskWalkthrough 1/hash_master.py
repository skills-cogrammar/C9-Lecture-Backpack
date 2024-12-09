import hashlib
import os


def hash_password(password):
    salt = os.urandom(16)
    # salt = "salty".encode()
    password = password.encode()
    hashed = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)

    with open('salts.txt', 'a') as file:
        file.write(f"salt: {salt.hex()}\nFull Hash: {hashed.hex()}")

    return salt + hashed


print(hash_password("VerySecurePassword9000!"))
