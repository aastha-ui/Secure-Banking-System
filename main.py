import json
from utils.auth import create_account, login
from utils.bank import menu

USERS_FILE = "data/users.json"

while True:
    print("\n=== Secure Banking System ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account(USERS_FILE)
    elif choice == "2":
        user = login(USERS_FILE)
        if user:
            menu(user, USERS_FILE)
    elif choice == "3":
        break
