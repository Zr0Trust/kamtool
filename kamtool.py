#!/bin/python3

import KAM
import KAM2

def kam_tool():
    print("=" * 50)
    print("KAM Tool")
    print("=" * 50)
    
    request = input("Welcome to the KAM Identity and Access Management tool for Linux.\nWould you like to create or delete a user?: ").lower()
    
    if request == "create":
        KAM.create_usr()
    elif request == "delete":
        KAM2.delete_usr()
    else:
        print("Invalid request. Please enter 'create' or 'delete'.")

# Call kam_tool to start the tool
kam_tool()
