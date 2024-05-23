'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# Simple Contact Book

CONTACTS_FILE = 'contacts.txt'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = [line.strip().split(',') for line in file.readlines()]
        return contacts
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts.append([name, phone, email])
    save_contacts(contacts)
    print(f"Contact {name} added.")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for contact in contacts:
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

def delete_contact(name):
    contacts = load_contacts()
    contacts = [contact for contact in contacts if contact[0] != name]
    save_contacts(contacts)
    print(f"Contact {name} deleted.")

def main():
    while True:
        print("\nSimple Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()
