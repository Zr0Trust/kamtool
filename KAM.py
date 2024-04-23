#!/bin/python3

import subprocess
import random
import string

def generate_password():
    length = 15  # You can adjust the length of the password as needed
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def create_usr():
    print("=" * 30)
    print("Create a User")
    print("=" * 30)

    usr = input("Please enter the new username: ")
    role = input("What role will this new user have? Admin, User, or Auditor?: ").lower()

    if role not in ["admin", "user", "auditor"]:
        print("Invalid input. Please choose from Admin, User, or Auditor.")
        return

    password = generate_password()

    print(f"Username: {usr}")
    print(f"Password: {password}")
    print(f"Role: {role}")

    # Create user account
    create_user(usr, password, role == "admin")  # Assign root privileges if role is admin

def create_user(username, password, root_privs=False):
    command = ['sudo', 'useradd', '-m', '-p', password, username]
    
    if root_privs:
        command.extend(['-g', 'sudo'])
    
    subprocess.run(command)
    
    print(f"User '{username}' created {'with root privileges' if root_privs else 'successfully'}.")

#while True:
    #create_usr()
    #break  # Break out of the loop after creating one user
