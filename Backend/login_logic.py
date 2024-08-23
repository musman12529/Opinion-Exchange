import data
import hashlib
import os


def hash_password(password, salt=None):
    """
    Hashes a password using PBKDF2-HMAC-SHA256.

    Args:
        password (str or bytes): The password to hash.
        salt (bytes, optional): The salt for the password hashing. If not provided, a random salt is generated.

    Returns:
        bytes: The hashed password.
    """
    if salt is None:
        salt = hashlib.sha256(os.urandom(32)).hexdigest().encode('ascii')

    if isinstance(password, str):
        password = password.encode('ascii')

    hashed_password = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    password_hash = salt + hashed_password
    return password_hash


def check_credentials(username, password):
    """
    Checks user credentials for login.

    Args:
        username (str): The username.
        password (str): The password.

    Returns:
        bool: True if the credentials are valid, False otherwise.
    """
    user = data.get_user(username)
    if not user:
        return False

    stored_password = user['passwordHash']

    if isinstance(stored_password, str):
        hashed_password = hash_password(stored_password)
        data.update_user(user['id'], user['username'], hashed_password, user['token'])

    user = data.get_user(username)

    stored_password = user['passwordHash']
    hashed_password = hash_password(password, stored_password[:64])

    result = stored_password == hashed_password

    if result:
        print("Login successful.")
    else:
        print("stored password:", stored_password)
        print("provided password:", password)
        print("Login failed. Passwords do not match.")

    return result


def register_account(username, password, confirm_password):
    """
    Registers a new user account.

    Args:
        username (str): The desired username.
        password (str): The password for the new account.
        confirm_password (str): The confirmation of the password.

    Returns:
        str: A message indicating the result of the registration.
    """
    user = data.get_user(username)
    if user:
        return "Username already exists. Please choose a different one."

    if password != confirm_password:
        return "Passwords do not match. Please try again."
    else:
        hashed_password = hash_password(password)

        data.create_user(username, hashed_password)
        return "Registration successful!"

