import hashlib
import getpass
import os

def hash_password(password):
    # Hash the password using sha256
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash

def create_account(username, password):
    # Store the hashed password in a file
    password_hash = hash_password(password)
    with open(f"{username}.txt", "w") as f:
        f.write(password_hash)

def login(username, password):
    try:
        with open(f"{username}.txt", "r") as f:
            password_hash = f.read()
    except FileNotFoundError:
        return False

    if hash_password(password) == password_hash:
        return True
    return False

def main():
    # Create account
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    create_account(username, password)

    # Log in
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if login(username, password):
        print("Access granted")
    else:
        print("Access denied")

if __name__ == "__main__":
    main()
