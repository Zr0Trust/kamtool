#!/bin/python3

import subprocess

def delete_usr():
    print("=" * 30)
    print("Delete a User")
    print("=" * 30)

    usr = input("Please enter the username you would like to delete: ").lower()
    verify = input(f"Are you sure you would like to permanently delete {usr}? Yes or No: ").lower()

    if verify == "yes":
        delete_user(usr)
    else:
        print("Exiting...")

def delete_user(username):
    command = ['sudo', 'userdel', '-r', '-f', username] # -r removes user home directory | -f forces the deletion
    
    subprocess.run(command)
    
    print(f"User '{username}' deleted successfully.")

