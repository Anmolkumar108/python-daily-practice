import json
import os

FILENAME = "contacts.json"

# Function to load contacts from a file
def load_contacts():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

# Function to save contacts to a file
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Enter your choice(1/2/3/4/5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts[name] = phone
        save_contacts(contacts)
        print("Contact added and saved successfully!")

    elif choice == "2":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"Phone number for {name}: {contacts[name]}")
        else:
            print("Contact not found!")

    elif choice == "3":   
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print("Contact deleted and updated in file!")
        else:
            print("Contact not found!")

    elif choice == "4":
        if contacts:
            print("\n===== ALL CONTACTS =====")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found!")

    elif choice == "5":
        print("Thank you for using the Contact Book!")
        break

    else:
        print("Invalid choice!")