# Define a list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added successfully!")

# Function to view the contact list
def view_contacts():
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    query = input("Enter the name or phone number to search: ")
    for contact in contacts:
        if query in contact['name'] or query in contact['phone']:
            print(f"Contact found: {contact['name']} - {contact['phone']}")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if name == contact['name']:
            print("Contact found. Update the details:")
            contact['phone'] = input("New phone number: ")
            contact['email'] = input("New email: ")
            contact['address'] = input("New address: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if name == contact['name']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Main menu loop
while True:
    print("\nContact Book Application")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")