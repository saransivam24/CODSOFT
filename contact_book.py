contacts={}
def add_contact(contacts):
    name=input("Enter name: ")
    number=input("Enter number: ")
    contacts[name]=number
    print("Contact added")
def view_contact(contacts):
    for name, number in contacts.items():
        print(name, ":", number)
def search_contact(contacts):
    name=input("Enter name: ")
    if name in contacts:
        print(name ,":",contacts[name])
    else:
        print("contact not found")
def delete_contact(contacts):
    name=input("Enter name: ")
    del contacts[name]
    print("Contact deleted")
while True:
    print("1.add contact")
    print("2.view contact")
    print("3.search contact")
    print("4.delete contact")
    print("5.Quit")
    choice=(input("Enter choice: "))
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contact(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        delete_contact(contacts)
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
