#Global dictionary to store contacts
contacts = {} #works in 1 and 2, just not printing keys & values in 2

#Option 1 to add new contact
def add_contact(): #works so far
    name = input("Please enter the contact's name: ")
    contacts[name] = {}

    phone_num = input("Please enter the contact's phone number: ")
    # contacts[name] = phone_num #think mess up is here

    email = input("Please enter the contact's email: ")
    contacts[name][phone_num] = email
    
    print(f"Contact for {name} added successfully.")
    return contacts

# Function to view all contacts
def view_contacts(): # <-- no parameter? works but two dif lines
    print("=== All Contacts ===")
    for name, contacts_list in contacts.items():
        print(f"{name}:")
        for phone_num, email in contacts_list.items():
            print("")
            print(f"Phone - {phone_num} Email - {email}")

# if len == 0:
    # print("No contacts found")

# Function to search for a contact by name
def search_name():
    name = input("Enter the name of the contact to search for:")
    if name in contacts:
      print(f"Contact found:{name} : Phone - {phone_num}, Email -") # same issue as viewing, keys/values not being called
    elif name not in contacts:
       print("Countact not found.")

# Function to remove a contact 
# #del method
#same as above for not in contacts

# Function to update a contact's information 
#.append?
#sane as above for not in contacts

# Main function to run the menu-driven system
def main():
    contacts = {}
    while True:
        print("---- Contact Manager ----")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Remove a Contact")
        print("5. Update a Contact")
        print("6. Quit")
        choice = int(input("Choose an option (1-6): "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        # elif choice == 4:
        #     remove_contact()
        # elif choice == 5:
        #     update_contact
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    main()

