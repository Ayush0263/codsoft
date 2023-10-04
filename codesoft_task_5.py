# WAP to make a contact book.
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print(f"Contact {name} added.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Name: {contact.name}, Phone: {contact.phone}")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted.")
                return
        print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n
