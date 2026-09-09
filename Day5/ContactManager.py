'''add
view
search
update
delete
exit'''
#name,phone,email'''
contacts=[]
def add_contact():
    name=input("Enter name:")
    phone=input("Enter phone:")
    email=input("Enter email:")
    if not validate_phone(phone):
        print("Invalid phone number.")
        return
    if not validate_email(email):
        print("Invalid email address.")
        return
    contact={"name":name,"phone":phone,"email":email}
    contacts.append(contact)
    print("Contact added successfully!")
def validate_phone(phone):
    if len(phone)==10 and phone.isdigit():
        return True
    else:
        return False
def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
def view_contacts():
    if len(contacts)==0:
        print("No contacts found.")
    else:
        for contact in contacts:
            print("================")
            print("Name:",contact["name"])
            print("Phone:",contact["phone"])
            print("Email:",contact["email"])
def search_contact():
    name=input("enter name to search:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            print("================")
            print("Name:",contact["name"])
            print("Phone:",contact["phone"])
            print("Email:",contact["email"])
            return
    print("Contact not found.")
def update_contact():
    name=input("Enter name to update:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            phone=input("Enter new phone:")
            email=input("Enter new email:")
            if not validate_phone(phone):
                print("Invalid phone number.")
                return
            if not validate_email(email):
                print("Invalid email address.")
                return
            contact["phone"]=phone
            contact["email"]=email
            print("Contact updated successfully!")
            return
    print("Contact not found.")
def delete_contact():
    name=input("Enter name to delete:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")
while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_contact()
    elif choice=="2":
        view_contacts()
    elif choice=="3":
        search_contact()
    elif choice=="4":
        update_contact()
    elif choice=="5":
        delete_contact()
    elif choice=="6":
        break
    else:
        print("Invalid choice. Please try again.")