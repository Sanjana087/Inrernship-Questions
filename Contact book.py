def add_contact(contacts, name, number):
    contacts[name] = number
    print(f"Contact {name} added successfully!")

def search_contact(contacts, name):
    if name in contacts:
        print(f"Name: {name}, Number: {contacts[name]}")
    else:
        print(f"Contact {name} not found!")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found!")

def list_contacts(contacts):
    if contacts:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("No contacts available!")

def main():
    contacts = {}

    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(contacts, name, number)
        elif choice == '2':
            name = input("Enter contact name to search: ")
            search_contact(contacts, name)
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            delete_contact(contacts, name)
        elif choice == '4':
            list_contacts(contacts)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
