#!/bin/python3

import subprocess
import random
import string
import os
import getpass


def generate_password():
    length = 15  # You can adjust the length of the password as needed
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


def add_user():
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

    create_usr()


def remove_user():
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
        command = ['sudo', 'userdel', '-r', '-f', username]  # -r removes user home directory | -f forces the deletion

        subprocess.run(command)

        print(f"User '{username}' deleted successfully.")

    delete_usr()


def generate_keys():
    def generate_ssh_keys(user, key_type='rsa', key_size=4096):
        # Define paths
        home_dir = f'/home/{user}'
        ssh_dir = os.path.join(home_dir, '.ssh')
        private_key_path = os.path.join(ssh_dir, 'id_rsa')
        public_key_path = os.path.join(ssh_dir, 'id_rsa.pub')

        # Create .ssh directory if it doesn't exist
        if not os.path.exists(ssh_dir):
            os.makedirs(ssh_dir, mode=0o700)

        # Generate SSH keys
        try:
            subprocess.run([
                'ssh-keygen',
                '-t', key_type,
                '-b', str(key_size),
                '-f', private_key_path,
                '-N', ''  # No passphrase
            ], check=True)
            print(f'SSH keys generated successfully for user {user}.')
        except subprocess.CalledProcessError as e:
            print(f'Error generating SSH keys: {e}')
            return False

        # Set correct permissions
        try:
            os.chmod(private_key_path, 0o600)
            os.chmod(public_key_path, 0o644)
            print(f'Permissions set for keys: {private_key_path} and {public_key_path}.')
        except OSError as e:
            print(f'Error setting permissions: {e}')
            return False

        return True

    if __name__ == '__main__':
        # Input the username
        user = input("Enter the username for whom to generate SSH keys: ").strip()

        # Verify the user exists
        if not os.path.exists(f'/home/{user}'):
            print(f'Error: User {user} does not exist.')
        else:
            # Generate SSH keys for the user
            generate_ssh_keys(user)


def kam_tool():
    print("=" * 50)
    print("KALI IAM Tool")
    print("=" * 50)

    print("Welcome to the Identity and Access Management tool for Kali Linux.")
    request = input(
        "\nPlease enter the letter for what action would you like to take?\n\na.add user\nb.delete user\nc.generate ssh keys?\n\nselection:").lower()


    if request == "a":
        add_user()
    elif request == "b":
        remove_user()
    elif request == "c":
        generate_keys()
    else:
        print("Invalid request. Please enter 'create' or 'delete'.")

# Call kam_tool to start the tool
kam_tool()
